print('\nWitaj w skrypcie do uzupełniania twardych html spacji za samogloskami jak "a, i, z..." w plikach html.\nZastępuje nietypowa spacje pliku Word, otwartego w Microsoft Teams.\nNowy plik ma nazwę [output.html]\n')
html_file = input('Wpisz nazwę pliku do uzupełnienia twardych spacji: ')
document = ''

with open(html_file, 'r+') as f:
    copy = f.read()


copyb = bytes(copy, 'utf8')
# \xc3\xa2\xe2\x82\xac\xc5\xbb to spacja w Word (Microsoft Teams), którą zmieniam na zwykłą spację
copyb = copyb.replace(b'\xc3\xa2\xe2\x82\xac\xc5\xbb', b' ')
copy = str(copyb, 'utf8')

ktory_char = 0
check = 3
check2 = 5
hardspace = ''
double_hardspace = ''


for line in copy:
    
    for char in line:
        if char == ' ' or char == '\n':
            samogloska = char + copy[ktory_char + 1] + copy[ktory_char + 2] + copy[ktory_char + 3] + copy[ktory_char + 4]
            
            if samogloska[1].isalpha() and samogloska[2] == ' ':
                # w sytuacji, gdy dwie samogloski po sobie, np: "i w tych okolicznościach..."
                if samogloska[3].isalpha() and samogloska[4] == ' ':
                    save = samogloska[3]
                    double_hardspace = samogloska[:-3] + '&nbsp;' + save + '&nbsp;'
                    print(double_hardspace)
                    document += samogloska[0]
                    check2 = 0

                elif check2 is not 2:
                    hardspace = samogloska[:-3] + '&nbsp;'
                    print(hardspace)
                    document += samogloska[0]
                    check = 0
            else:
                    document += samogloska[0]
        else:
            document += char

        # wartownik okresla, czy zamienic na samogloske z twarda spacja
        if check == 2:
            document = document[:-3] + hardspace

        if check2 == 4:
            document = document[:-5] + double_hardspace
        
        ktory_char += 1
        check += 1
        check2 += 1


with open('output.html', 'w') as outf:
    outf.write(document)

print('Twarde spacje zostały dodane. Zajrzyj do pliku output.html\n')
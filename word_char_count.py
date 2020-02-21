n1 = 0
n2 = 0

with open('tekst.txt') as file:
    for line in file:
        n1 += len(line)
        n2 += len(line.split())

print('char count: ', n1)
print('word count: ', n2)
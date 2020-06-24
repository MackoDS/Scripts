# Ten skrypt sprawdza prawdopodobieństwo, że pliki, których rozmiary zostały zapisane nie były zebrane losowo
# zgodnie z Rozkładem Benforda

import os
import math
import pandas as pd

df = pd.DataFrame(columns=['nazwa', 'współczynnik'])

for f in os.listdir('./Files_to_check'):
    all_numbers_count = 0
    # otwiera każdy plik txt i liczy ilość poszczególnych cyfr na pierwszym miejscu w każdej linii
    if f[-4:] == '.txt':
        with open('./Files_to_check/{}'.format(f), 'r') as numbers:
            data = numbers.read().split()
        
            # zlicza wszystkie liczby oraz sumuje ich poszczególne pierwsze cyfry
            numbers_in_file_count = len(data)
            
            # tworzy listę z pierwszymi cyframi każdej liczby
            first_digits = [digit[0] for digit in data]


            # lista zawierająca liczbę poszczególnych pierwszych cyfr, odpowiednio dla cyfr: 1, 2, 3, 4, 5, 6, 7, 8, 9.
            # => np. first_digits_count[0] zwraca liczbę jedynek na pierwszym miejscu w kolejnych liczbach
            first_digits_count = [first_digits.count(char) for char in '123456789']

            # oblicza procentowe występowanie poszczególnych pierwszych cyfr w pliku, odpowiednio dla cyfr: 1, 2, 3, 4, 5, 6, 7, 8, 9
            data_percentage = [first_digits_count[i] / numbers_in_file_count * 100 for i in range(len(first_digits_count))]
            
            
            # oczekiwane procentowe występowanie dla 1, 2, 3, 4, 5, 6, 7, 8, 9 według Prawa Benforda
            expected_percentage = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
            cheating_probability = 0

            # oblicza różnicę pomiędzy oczekiwanym procentowym występowaniem pierwszych cyfr a a tym w pliku
            exp_act_diff = [math.fabs(expected_percentage[i] - data_percentage[i]) for i in range(len(data_percentage))]
            # sumuje różnice między występowaniem w pliku a prawem Benforda
            cheating_probability = round(sum(exp_act_diff), 0) / 100
            if cheating_probability > 1:
                cheating_probability = 1

            # sprawdza, czy ktoś ręcznie wpisując liczb nie zaczął liczby od 0, np: 013
            for number in data:
                if len(number) > 1:
                    if number[0] == '0':
                        cheating_probability = 1
            

            new_row = {'nazwa': f, 'współczynnik': cheating_probability}
            df = df.append(new_row, ignore_index=True)
            

df = df.sort_values(by=['współczynnik'])
df['liczba porządkowa'] = range(1, len(df) + 1)
df = df.sort_values(by=['nazwa'])

# zapisuje utworzony dataframe w pliku csv
df.to_csv('cheating probability.csv', sep=',', encoding='utf-8-sig', index=False)
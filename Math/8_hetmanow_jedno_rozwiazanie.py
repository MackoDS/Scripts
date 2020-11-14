#python3
import numpy as np


# czyMoznaPostawicHetmana prawdza czy hetman może stać na polu y, x
def czyMoznaPostawicHetmana(szachownica, y, x):
    #dlugosc boku szachownicy
    a = len(szachownica)
    
    for i in range(a):
        # jeśli istnieje hetman na kolumnie x
        if szachownica[i][x] == 1:
            return False

    for i in range(a):
        # jeśli istnieje hetman na kolumnie y
        if szachownica[y][i] == 1:
            return False
        
    for i in range(a):
        for j in range(a):

            # jeśli na polu stoi hetman
            if szachownica[i][j] == 1:
                # szuka innego hetmana na przekątnej
                if abs(j - x) == abs(i - y):
                    return False
    # jeśli przeszło wszystkie testy, można postawić hetmana
    return True



def rozwiaz(szachownica, rzad=0):
    
    a = len(szachownica)

    # stawiam hetmana na kazdym polu, na ktorym jest to możliwe w rzedzie i stosuję rekurencję
    for x in range(a):

        if czyMoznaPostawicHetmana(szachownica, rzad, x):
            # jesli mozna postawic hetmana, stawiam go
            szachownica[rzad][x] = 1

            
            # rekurencja
            rozwiaz(szachownica, rzad + 1)
            #sprawdzam czy na szachownicy stoi liczba hetmanow rowna dlugosci boku szachownicy
            if sum(sum(h) for h in szachownica) == a:
                return szachownica

            #usuwam poprzednio ustawionego hetmana
            szachownica[rzad][x] = 0
            


def hetmani(n):
    szachownica = np.zeros([n,  n],  dtype = int)
    szachownica = szachownica.tolist()

    rozwiazanie = rozwiaz(szachownica)
    print(np.matrix(szachownica))
    



if __name__ == "__main__":
    n = input("Jakiej długości jest bok szachownicy oraz jaka jest liczba hetmanów? ")
    n = int(n)
    hetmani(n)

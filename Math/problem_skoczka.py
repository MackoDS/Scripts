#python3
import numpy as np


def czyMoznaPostawicSkoczka(x, y, szachownica):
    n = len(szachownica)
    # sprawdzam czy ruch miesci się w szachownicy oraz czy skoczek nie stał już na tym polu
    if(x >= 0 and y >= 0 and x < n and y < n and szachownica[y][x] == -1):
        return True
    return False



def rozwiaz(szachownica, wsp_x, wsp_y, ruch_x, ruch_y, nr_pozycji):
    n = len(szachownica)
    # jeżeli skoczek przeszedl po wszystkich polach wyjscie z rekurencji
    if(nr_pozycji == n**2):
        return True

    # skoczek moze wykonac 8 roznych ruchow
    for i in range(8):
        nowy_x = wsp_x + ruch_x[i]
        nowy_y = wsp_y + ruch_y[i]

        if(czyMoznaPostawicSkoczka(nowy_x, nowy_y, szachownica)):
            szachownica[nowy_y][nowy_x] = nr_pozycji

            if(rozwiaz(szachownica, nowy_x, nowy_y, ruch_x, ruch_y, nr_pozycji + 1)):
                return True

            szachownica[nowy_y][nowy_x] = -1
    return False



def skoczek(nr_ruchu, wsp_x, wsp_y):
    n = 8
    # tworze szachownice
    szachownica = np.full([n,  n], -1,  dtype = int)
    szachownica = szachownica.tolist()

    # odejmuje 1, poniewaz wspolrzedne x i y bylyby indeksowane od 0
    wsp_y -= 1
    wsp_x -= 1

    # reprezentacja możliwych ruchow skoczka (oś x i y)
    # w kolejnosci odpowiadajacej {{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}}
    ruch_x = [-2, -1, 1, 2, 2, 1, -1, -2,]
    ruch_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # stawiam skoczka na pierwszym polu
    szachownica[wsp_y][wsp_x] = 0
    nr_pozycji = 1

    wsp_y = wsp_y + ruch_y[nr_ruchu]
    wsp_x = wsp_x + ruch_x[nr_ruchu]

    # wykonuje pierwszy ruch - jego numer podany jest w wywolaniu skoczek(nr_ruchu, wsp_x, wsp_y)
    if czyMoznaPostawicSkoczka(wsp_x + ruch_x[nr_ruchu], wsp_y + ruch_y[nr_ruchu], szachownica):
        szachownica[wsp_y][wsp_x] = nr_pozycji
        nr_pozycji += 1
    else:
        print("Nie możesz rozpoczac takim ruchem")
        return
    

    # rozpoczynam rekurencje
    if(not rozwiaz(szachownica, wsp_x, wsp_y, ruch_x, ruch_y, nr_pozycji)):
        print("Rozwiazanie nie istnieje")
    else:
        print(np.matrix(szachownica))



if __name__ == "__main__":
    skoczek(2, 1, 1)

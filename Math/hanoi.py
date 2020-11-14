#python3

# Algorytm rozwiazujacy problem wiezy hanoi
# Wywolanie: hanoi(liczba_kolkow, kolek z ktorego przekladamy, kolek na ktory chcemy przelozyc, posredni kolek)


def hanoi(n, pierwszy, docelowy, posredni):
    if n == 1:
        print("{} -> {}".format(pierwszy, docelowy))
        
    else:
        hanoi(n - 1, pierwszy, posredni, docelowy)

        print("{} -> {}".format(pierwszy, docelowy))
        hanoi(n - 1, posredni, docelowy, pierwszy)




if __name__ == "__main__":
    hanoi(20, "A", "C", "B")
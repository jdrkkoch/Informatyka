import random
def wyszukiwanie_polowkowe(lista, liczba):
    lewy = 0
    prawy = len(lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == liczba:
            return True
        elif lista[srodek] < liczba:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return False
rozmiar_listy = 20
lista = random.sample(range(1, 101), rozmiar_listy)
lista.sort()
print("Wygenerowana lista:", lista)
liczba = int(input("Podaj liczbę do wyszukania: "))
if wyszukiwanie_polowkowe(lista, liczba):
    print(f"Liczba {liczba} znajduje się w liście.")
else:
    print(f"Liczba {liczba} nie znajduje się w liście.")

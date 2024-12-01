print("Zadanie 60")
liczby = []
liczby_mniejsze_1000 = []
licznik = 0

with open("liczby.txt", "r") as plik:
    for linia in plik:
        liczba = int(linia)
        if liczba < 1000:
            licznik += 1
            liczby_mniejsze_1000.append(liczba)
        liczby.append(liczba)

ostatnie_dwie = liczby_mniejsze_1000[-2:]

print(licznik)
print(ostatnie_dwie)

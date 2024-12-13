def czy_arytmetyczny(ciag):

    roznica = ciag[1] - ciag[0]
    for i in range(1, len(ciag)):
        if ciag[i] - ciag[i - 1] != roznica:
            return False
    return True


with open("ciagi.txt", "r") as plik:
    linie = plik.readlines()

ciagi = []
i = 0
while i < len(linie):
    liczba_wyrazow = int(linie[i].strip())
    ciag = linie[i + 1].strip().split()

    ciag_liczb = []
    for liczba in ciag:
        ciag_liczb.append(int(liczba))

    ciagi.append(ciag_liczb)
    i += 2

ilosc_arytmetycznych = 0
najwieksza_roznica = 0
ciag_najwieksza_roznica = []

for ciag in ciagi:
    if czy_arytmetyczny(ciag):
        ilosc_arytmetycznych += 1
        roznica = ciag[1] - ciag[0]
        if roznica > najwieksza_roznica:
            najwieksza_roznica = roznica
            ciag_najwieksza_roznica = ciag

print(ilosc_arytmetycznych)
print(najwieksza_roznica)
print(ciag_najwieksza_roznica)

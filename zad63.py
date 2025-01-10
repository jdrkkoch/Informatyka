def horner(liczba,x):
    w = int(liczba[0])
    for i in range(1,len(liczba)):
        w = x * w + int(liczba[i])
    return w


ciagi = []
with open("ciagi.txt") as plik:
    for linia in plik:
        ciagi.append(linia.strip())
print(ciagi)
for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])
licznik = 0
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik+= 1
print(licznik)

liczby = []
for i in range(len(ciagi)):
    liczby.append(horner(ciagi[i,2]))
print(liczby)

sito = []
for i in range(363000):
    sito.append(1)
for i in range(2, 363000):
    if sito[i] == 1:
        for j in range(i+i, 363000,i):
            sito[j] = 0
pierwsze = []
for j in range(2, 363000, i):
    if sito[i] == 1:
        pierwsze.append(i)
    print(pierwsze)

for i in range(len(liczby)):
    czynniki = []
    for j in range(len(pierwsze[j])) == 0:
        czynniki.append(pierwsze[j])
        liczba = liczba // pierwsze[j]
        if len(czynniki) > 2:
            break
    if len(czynniki) == 2:
        print(liczby[i],czynniki)



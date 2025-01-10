def horner(liczba,x):#liczba - string, x - system w którym jest liczba w = int(liczba[0])
for i in range(1,len(liczba)):
    w = x * w + int(liczba[i])
    return w

def decToAll(liczba,system):
    wynik = ""
while liczba > 0:
    wynik = str(liczba%system) + wynik
    liczba = liczba // system
    return(wynik)

liczby8 = []
with open("liczby1.txt") as plik:
    for linia in plik:
        liczby8.append(linia.strip())
print(liczby8)
minimum = int(liczby8[0])
maks = int(liczby8[0])
for i in range(1, len(liczby8)):
    if minimum > int(liczby8[i]):
        minimum = int(liczby8[i])
    if maks < int(liczby8[i]):
        maks = int(liczby8[i])
print(minimum, maks)
pierwszy = int(liczby8[0])
ilosc = 1
for i in range(len(liczby8)-1):
    if int(liczby8[i])<=int(liczby8[i+1]):
        ilosc+= 1
        if ilosc > maksymalnailosc:
            maksymalnailosc = ilosc
            pierwszymaks = pierwszy
    else:
        pierwszy = int(liczby8[i+1])
        ilosc = 1
    print(maksymalnailosc, pierwszymaks)
def horner(liczba,x):
    w = int(liczba[0])
    for i in range(1,len(liczba)):
        w = x * w + int(liczba[i])
    return w
def dectoall(liczba,system):
    wynik = ("")
    while liczba > 0:
        wynik = str(liczba%system) + wynik
        liczba = liczba // system
    return(wynik)
print(dectoall(449,8))
print(horner("11010", 2))
print(horner("701", 8))
print(horner("302", 4))
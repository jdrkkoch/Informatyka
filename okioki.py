def funkcja(x):
    return x**2 - 4

def znajdz_miejsce_zerowe(a, b, dokladnosc=0.0001):

    while (b - a) > dokladnosc: 
        srodek = (a + b) / 2
        if funkcja(srodek) == 0:
            return srodek
        elif funkcja(a) * funkcja(srodek) < 0:
            b = srodek
        else:
            a = srodek
    return (a + b) / 2


a = 0
b = 3
miejsce_zerowe = znajdz_miejsce_zerowe(a, b)
print("Miejsce zerowe funkcji to:", miejsce_zerowe)

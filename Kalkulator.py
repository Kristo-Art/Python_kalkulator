# kalkulator.py
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero"

# Przykłady użycia:
print(dodaj(2, 30))
print(odejmij(5, 24))
print(pomnoz(4, 63))
print(podziel(8, 2))

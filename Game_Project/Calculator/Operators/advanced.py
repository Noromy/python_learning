import math

def pangkat(a, b):
    return a ** b

def akar(a):
    if a < 0:
        raise ValueError("Bilangan Negatif tidak bisa di akarkan")
    return math.sqrt(a)
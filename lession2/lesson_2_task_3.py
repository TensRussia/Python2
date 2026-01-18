import math


def square(a):
    a = math.ceil(a)
    return (a**2)


stor = float(input("длина стороны: "))
result = square(stor)
print(result)

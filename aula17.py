def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

variavel_1 = soma(1, 2, 3, 4)
variavel_2 = soma(1, 10, 16, 4, 54, 85, 2)
variavel_3 = soma(1, 10, 16, 4, 54, 85, 2, 1, 2 ,3, 4)
print(variavel_1)
print(variavel_2)
print(variavel_3)
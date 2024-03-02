def duplicar_numero(numero):
    return numero * 2

def triplicar_numero(numero):
    return numero * 3

def quadruplicar_numero(numero):
    return numero * 4

duplicar_1 = print(duplicar_numero(3))
triplicar_1 = print(triplicar_numero(2))
quadruplicar_1 = print(quadruplicar_numero(1.5))

# Como são funções similares podemos substituir pela abaixo

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(3))
print(triplicar(2))
print(quadruplicar(1.5))
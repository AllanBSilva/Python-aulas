# Desempacotamento de lista

lista = ['Allan', 'Bezerra', 'da', 'Silva']
lista_2 = ['Allan', ['Bezerrda', 'da', 'Silva'], 34]

print(*lista)
print(*lista_2, sep="\n")
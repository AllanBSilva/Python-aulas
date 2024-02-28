'''
split - divide uma string
join - une uma string
'''

frase = 'Olha como quebrar uma frase, legal'

lista_palavras_1 = frase.split()
lista_palavras_2 = frase.split(',')
print(lista_palavras_1)
print(lista_palavras_2)

for i, frase in enumerate(lista_palavras_2):
    print(lista_palavras_2[i].strip())

frase_unidas = '-'. join(lista_palavras_2)
print(frase_unidas)
'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero = input('Digite um número para saber o dobro dele: ')

try:
    numero = int(numero)
    print('INT:', numero)
    print(f'O dobro do {numero} é {numero * 2}')
except:
    print('O dado digitado não é um número')
    
#Outra forma de fazer

if numero.isdigit():
    print('INT:', numero)
    print(f'O dobro do {numero} é {numero * 2}')
else:
    print('O dado digitado não é um número')
    
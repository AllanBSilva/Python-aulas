# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = d1.copy() Copia rasa, as listas ainda permanecem com mesmo end de memória
d2 = copy.deepcopy(d1) # Mesmo alterando a lista, elas agora são diferentes

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1['c1'])
print(d1.get('c1'))
print(d1.get('c1', 'Não existe'))
print(d1.get('c3', 'Não existe'))
apaga_especifico = d1.pop('c2')
print(apaga_especifico)
apaga_ultima_chave = d2.popitem()
print(apaga_ultima_chave)
print(d1)
print(d2)
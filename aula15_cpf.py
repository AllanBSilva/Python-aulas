# Validar CPF '213.667.890-67'

import sys

cpf_informado = '213.667.890-67'
cpf_sem_ponto = cpf_informado
cpf_digito_dez = ''
cpf_digito_onze = ''
resultado_digito_dez = 0
resultado_digito_onze = 0
contador_regressivo_1 = 10
contador_regressivo_2 = 11
cpf_calculado = ''

entrada_e_sequencial = cpf_informado == cpf_informado[0] * len(cpf_informado)

if entrada_e_sequencial:
    print('CPF digitado não é válido')
    sys.exit()

for i in ('.','-'):
    cpf_sem_ponto = cpf_sem_ponto.replace(i, '')

'''
cpf_sem_ponto = cpf_sem_ponto.replace('.', '').replace('-', '') 
Funciona da mesma forma de cima.
'''
'''
import re

cpf_sem_ponto = re.sub(r'[^0-9], '', cpf_sem_ponto)
Funciona da mesma forma de cima.
'''

cpf_digito_dez = cpf_sem_ponto[0:9]

for indice in cpf_digito_dez:
    resultado_digito_dez += int(indice) * contador_regressivo_1
    contador_regressivo_1 -= 1

decimo_digito = (resultado_digito_dez *10) % 11

decimo_digito = decimo_digito if decimo_digito <= 9 else 0

#print(decimo_digito)

cpf_digito_onze = cpf_sem_ponto[0:10]

for indice in cpf_digito_onze:
    resultado_digito_onze += int(indice) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_onze = (resultado_digito_onze *10) % 11

digito_onze = digito_onze if digito_onze <= 9 else 0

#print(digito_onze)

cpf_calculado = cpf_digito_dez + str(decimo_digito) + str(digito_onze)

if cpf_sem_ponto == cpf_calculado:
    print('CPF válido!')
else:
    print('CPF Inválido')



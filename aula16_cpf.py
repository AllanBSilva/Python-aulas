# Gerador de CPF'

import random

nove_digitos = ''
cpf_digito_onze = ''
resultado_digito_dez = 0
resultado_digito_onze = 0
contador_regressivo_1 = 10
contador_regressivo_2 = 11
cpf_calculado = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

for indice in nove_digitos:
    resultado_digito_dez += int(indice) * contador_regressivo_1
    contador_regressivo_1 -= 1

decimo_digito = (resultado_digito_dez *10) % 11

decimo_digito = decimo_digito if decimo_digito <= 9 else 0

cpf_digito_onze = nove_digitos + str(decimo_digito)

for indice in cpf_digito_onze:
    resultado_digito_onze += int(indice) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_onze = (resultado_digito_onze *10) % 11

digito_onze = digito_onze if digito_onze <= 9 else 0

cpf_calculado = nove_digitos + str(decimo_digito) + str(digito_onze)

print(cpf_calculado)



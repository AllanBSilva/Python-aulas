import os

palavra_secreta = 'all'
letra_digitada = ''
letras_acertadas = ''

contador_tentativas = 0

while True:
    palavra_formatada = ''
    letra_digitada = input('Digite uma letra: ')
    contador_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'
              
    print(f'Palavra formatada: {palavra_formatada}')
    
    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU PARABÉNS!!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {contador_tentativas}')
        letras_acertadas = ''
        contador_tentativas = 0

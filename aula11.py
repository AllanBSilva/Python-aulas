import os

lista = []
lista_2 = ['a','i','l']

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]listar: ').lower()
    print(opcao)
    
    if opcao not in lista_2:
        continue
    
    if opcao == 'i':
        os.system("cls")
        nome_inserir = input('Valor: ')
        lista.append(nome_inserir)
        
    elif opcao == 'a':
        os.system("cls")
        indice = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice)
            lista.pop(indice)
        except ValueError:
            print('Por favor digite um número inteiro!')
        except IndexError:
            print('Índice não existe na lista!')
        except Exception:
            print('Erro desconhecido!')
            
    elif opcao == 'l':
        os.system("cls")
        if (lista):
            for i,j in enumerate(lista):
                print(i, j)
        else:
            print('Lista vazia')
    
    
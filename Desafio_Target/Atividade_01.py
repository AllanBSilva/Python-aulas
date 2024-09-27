import os
import random

def fibonacci_sequence(n):
    sequence = [0, 1]
    while True:
        next_fib = sequence[-1] + sequence[-2]
        if next_fib > n:
            break
        sequence.append(next_fib)
    return sequence

def check_fibonacci(num):
    if num < 0:
        return False
    fib_sequence = fibonacci_sequence(num)
    return num in fib_sequence

os.system('cls' if os.name == 'nt' else 'clear')
print("-" * 80)
print("Vamos verificar se um número está contido na sequência de Fibonacci.")
print("-" * 80)

def get_user_input():
    print("-" * 80)
    while True:
        user_input = input("Informe um número: ")
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    while True:
        print("[1] - Deseja informar um número \n[2] - Utilizar um número pré-definido\n[3] - Utilizar um número aleatório")
        choice = input("Escolha uma opção: ")

        match choice:
            case '1':
                number = get_user_input()
                break
            case '2':
                print("-" * 80)
                number = 21
                print(f"Número pré-definido: {number}")
                break
            case '3':
                print("-" * 80)
                number = random.randint(1, 100)
                print(f"Número aleatório gerado: {number}")
                break
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-" * 80)
                print("Opção inválida! Escolha uma opção válida.")
                print("-" * 80)
                continue

    if check_fibonacci(number):
        print(f"\nO número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"\nO número {number} não pertence à sequência de Fibonacci.")

    print("-" * 80)

main()

'''🧩 Missão 3: Par ou Ímpar
🎯 Desafio:

    Peça um número inteiro ao usuário.

    Diga se ele é par ou ímpar.'''

while True:
    try:         
        num = int(input('Digite um número inteiro\nou zero para encerrar a execução do programa: '))
        if num == 0:
            print(f'programa encerrado pois você digitou {num}')
            break
        if num % 2 == 0:
            print(f'o número {num} é um número par.')
        else:
               print(f'o número {num} é um número impar.')
    except ValueError:
        print('você digitou algo que não é um numéro inteiro')
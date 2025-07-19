'''🎯 Tema do Dia: Condicionais (if, elif, else)
🧩 Missão 1: Detector de Número Positivo, Negativo ou Zero

    Peça um número ao usuário e diga se ele é positivo, negativo ou zero.'''

while True:
    try:
        numero = float(input('Olá usuário, me diga um número (digite zero para sair):\n'))
    
        if numero > 0:
            print('número positivo\n')
        elif numero < 0:
            print('número negativo\n')
        elif numero == 0:
            print('o número em questão é zero, até logo\n')
            break
        else:
            print('se você está lendo isso é porque provavelmente não digitou zero, um número positivo, ou negativo!\n')
    except ValueError:
        print('digite somente números')
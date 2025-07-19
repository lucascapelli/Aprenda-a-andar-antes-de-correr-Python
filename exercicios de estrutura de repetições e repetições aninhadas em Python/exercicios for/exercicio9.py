#Escreva um programa que mostre todos os números primos entre 1 e 50.
for num in range(2, 51):  # de 2 até 50
    divisores = 0
    for i in range(1, num + 1):  # verifica todos os números que podem dividir o num
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        print(num)

# O programa verifica quantos divisores cada número tem.
# Se ele só for divisível por 1 e por ele mesmo, é considerado primo.

#Exercício 9 — Contador de pares e ímpares
#Escreva um programa que peça ao usuário para digitar 10 números inteiros.
#Ao final, o programa deve mostrar:
#Quantos números pares foram digitados,
#Quantos números ímpares foram digitados.

pares = 0
impares = 0
contador = 0

while contador <= 10:
    contador += 1
    num = int(input("digite um numero: "))
    if num % 2 == 0:
        pares += 1
        print(f" o numero {num} é um numero par")
    else:
        impares += 1
        print(f" o numero {num} é um numero impar")

print(f"\n o total é de:\n numeros pares: {pares}\n numeros impares: {impares}")

input("digite enter para sair")
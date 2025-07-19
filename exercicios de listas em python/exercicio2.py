lista = []
pares = 0
impares = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"o total de números pares é de {pares} e de ímpares é de {impares} é a lista total \n {lista}")
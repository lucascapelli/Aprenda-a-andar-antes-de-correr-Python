contador = 0
positivo = 0
negativo = 0
menor = None

for i in range(1,11):
    valor = float(input("digite um valor real: "))
    contador += 1
    if valor > 0:
        positivo += 1
        print(f"{valor} é positivo")
    else:
        negativo += 1
        print(f"{valor} é negativo")
    if menor is None or valor < menor:
        menor = valor

print(f"dos {contador} valores descritos:\n{positivo} são positivos\n{negativo} são negativos\n e o menor valor é: {menor}")
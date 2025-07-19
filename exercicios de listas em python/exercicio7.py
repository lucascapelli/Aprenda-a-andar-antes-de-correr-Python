numeros = [4, 9, 1, 3, 7, 6, 2]
nova_lista = []

# 1. Imprima cada número da lista multiplicado por 2.
for i in range(7):
    print(f"Número da primeira lista na posição {i} multiplicado por 2: {numeros[i] * 2}")
    if numeros[i] % 2 == 0:
        nova_lista.append(numeros[i] * 3)  # Adiciona já multiplicado por 3

print()
# 2. Mostra a nova lista
print(f"Nova lista constituída pelos números pares da primeira lista, multiplicados por 3:\n{nova_lista}")

# 3. Soma da nova lista
soma = sum(nova_lista)
print(f"Soma da nova lista: {soma}")

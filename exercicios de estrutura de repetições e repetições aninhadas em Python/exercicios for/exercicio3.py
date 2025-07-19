# Imprimir todos os números de 1 a 50 que são múltiplos de 3

for i in range(1, 51):
    if i % 3 == 0:
        print(i)

# Passamos por todos os números de 1 até 50.
# Em cada número, verificamos se ele é múltiplo de 3 (ou seja, se i % 3 == 0(o que quer dizer que se o resto divisão dele por três é igual a 0 faça até 50)).
# Se for, imprimimos o número.

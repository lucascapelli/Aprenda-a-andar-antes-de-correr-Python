# Criando lista vazia
numeros = []

# Lendo 5 números do usuário
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

# Calculando maior, menor e média
# max() → retorna o maior valor da lista
# min() → retorna o menor valor da lista
# sum() → retorna a soma dos valores da lista
# len() → retorna a quantidade de elementos na lista
maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

# Exibindo os resultados
print("\n--- Resultados ---")
print("Números digitados:", numeros)
print("Maior número:", maior)
print("Menor número:", menor)
print("Média:", media)

# Dada a lista abaixo, faça:
valores = [10, 5, 7, 2, 8, 10]

# a) Qual é a soma de todos os valores?
# b) Qual o maior e o menor valor?
# c) Quantas vezes o número 10 aparece?
 
soma = sum(valores)
maior = max(valores)
menor = min(valores)
valor_aparece = valores.count(10)

print(f"lista de valores {valores}")
print(f"soma de todos os valores {soma}")
print(f"maior valor da lista de valores {maior}")
print(f"menor valor da lista de valores {menor}")
print(f"quantas vezes aparece o valor 10 da lista de valores {valor_aparece}")
idades = [12, 17, 18, 24, 16, 30, 15, 22]
pode_ser_preso = 0
nn_pode_ser_preso = 0
menor_de_idade = []
media = sum(idades) / len(idades)


# 1. Conte quantas pessoas são maiores de idade (18 anos ou mais).
# 2. Crie uma nova lista apenas com as idades dos menores de idade.
# 3. Mostre a média de idade de todos os elementos da lista original.

for i in range(len(idades)):
    if idades[i]>=18:
        pode_ser_preso+=1
    else:
        nn_pode_ser_preso+=1
        menor_de_idade.append(idades[i])

print(f"lista original\n{idades}")
print(f"quantidade de pessoas da lista original que são maiores de 18:\n {pode_ser_preso}")
print(f"quantidade de pessoas da lista original que são menores de 18:\n {nn_pode_ser_preso}")
print(f"lista de pessoas menores de idade\n {menor_de_idade}")
print(f"média de idade da lista original {media}")
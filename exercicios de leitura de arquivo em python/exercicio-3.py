'''
Exercício:

    Crie um script em Python que:
    1️⃣ Abra o arquivo texto chamado "arquivo_para_exercicios_de_leitura.txt" no modo leitura.
    2️⃣ Leia o arquivo linha por linha.
    3️⃣ Conte quantas linhas existem no arquivo.
    4️⃣ Imprima cada linha sem quebras de linha extras (use .strip()).
    5️⃣ No final, imprima:

Total de linhas: X

Onde X é o número de linhas.
'''
contador = 0

with open('exercicios de leitura de arquivo em python/exercicio-1-2-3.txt','r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
        contador+=1

print(f'Total de linhas: {contador}')
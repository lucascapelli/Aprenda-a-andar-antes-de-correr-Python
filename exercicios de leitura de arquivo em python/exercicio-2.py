contador = 0

with open('exercicios de leitura de arquivo em python/exercicio-1-2-3.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
        contador += 1

print(f'O arquivo tem {contador} linhas.')

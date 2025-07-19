'''
Exercício

Arquivo: exercicio-7.txt (uma frase por linha)

Tarefa: Ler o arquivo e contar o total de palavras em todo o arquivo.

Dica: Use .split() para separar palavras.
'''
armazenador = 0

with open('exercicios de leitura de arquivo em python/exercicio-7.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip().split()
        palavras = len(linha)
        armazenador+=palavras

print(armazenador)
'''
Exercício — Contar ocorrências de cada palavra no arquivo

Arquivo: frases.txt

Tarefa: Criar um dicionário onde a chave é a palavra e o valor é a quantidade de vezes que ela aparece no arquivo.
'''
from collections import defaultdict
contador = defaultdict(int)

with open('exercicios de leitura de arquivo em python/exercicio-8.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip().split()
        if linha == "": continue

        for item in linha:
            contador[item] += 1

duplicados = {k: v for k, v in contador.items() if v > 1}
print(f'\nItens repetidos com suas contagens:\n{duplicados}') 
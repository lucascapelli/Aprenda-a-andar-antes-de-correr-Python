'''
Exercício

Enunciado:

    Crie um script em Python que:
    1️⃣ Abra o arquivo chamado "notas_alunos.txt" no modo leitura.
    2️⃣ Cada linha do arquivo tem o formato:

nome,nota

Exemplo de conteúdo:

Ana,8.5
Bruno,7.2
Carlos,9.0

3️⃣ Leia todas as linhas do arquivo.
4️⃣ Para cada linha, separe o nome e a nota.
5️⃣ Imprima:

Aluno: <nome> - Nota: <nota>

6️⃣ Conte quantos alunos tem no arquivo.
7️⃣ Ao final, imprima:

Total de alunos: X

'''

alunos = 0

with open('exercicios de leitura de arquivo em python/exercicio-4.txt', 'r') as arquivo:
      for linha in arquivo:
        linha = linha.strip()
        if linha == "":
            continue

        nome, nota = linha.split(',')
        print(f'Aluno: {nome} - Nota: {nota}')
        alunos += 1

print(f'Total de alunos: {alunos}')
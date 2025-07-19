'''
🧭 Exercício

Crie um script em Python que:

✅ 1️⃣ Abra um arquivo chamado "produtos.txt" no modo leitura.

✅ 2️⃣ Cada linha do arquivo tem o formato:

nome_produto,preco

✅ Exemplo de conteúdo:

Arroz,5.50
Feijão,7.20
Macarrão,4.00

✅ 3️⃣ Leia todas as linhas do arquivo.

✅ 4️⃣ Para cada linha:

    Separe o nome do produto e o preço.

    Converta o preço para float.

    Acumule o preço em um total geral.

✅ 5️⃣ Imprima para cada linha:

Produto: <nome> - Preço: <preco>

✅ 6️⃣ Ao final, imprima:

Total geral: <soma dos preços>

'''

total = 0

with open('exercicios de leitura de arquivo em python/exercicio-5.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha == "": continue

        nome, preco = linha.split(',')
        preco_convertido = float(preco)
        print(f'Produto: {nome} - Preço: {preco_convertido}')
        total += preco_convertido

print(f'Total geral: {total}')
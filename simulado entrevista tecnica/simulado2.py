'''
🧠 EXERCÍCIO 2 — FILTRO

Você recebeu uma lista de dicionários representando livros:

[
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9}
]

TAREFA:

Crie uma função que:

Receba a lista de livros

Retorne apenas os livros com preço menor que 40
'''
lista =[
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9}
]

# Função que filtra a lista de livros retornando apenas os com preço < 40
def filtro(livros):
    # cria uma lista vazia que conterá os livros filtrados
    filtrados = []
    # percorre cada item da lista de livros (cada item é um dicionário)
    for i in livros:    # livro é um dicionário
        # acessa a chave 'preco' do dicionário e compara com 40
        if i["preco"] < 40:
            # adiciona o dicionário inteiro à lista de resultados
            filtrados.append(i)  # adiciona o livro inteiro

    # retorna a lista com os livros que atenderam à condição
    return filtrados

# imprime o resultado do filtro aplicado à lista de exemplo
print(filtro(lista))
'''
🧠 Exercício Extra 2 — Filtrar por preço e título

Você tem a lista de livros:

livros = [
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9},
  {"titulo": "O Pequeno Príncipe", "preco": 19.9},
  {"titulo": "O Senhor dos Anéis", "preco": 59.9}
]

TAREFA:
Crie uma função que:

Receba a lista de livros.

Retorne apenas os livros que:

Tenham preço menor que 50 e

Tenham título com mais de 10 caracteres.
'''

# lista de livros — cada item é um dicionário com título e preço
livros = [
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9},
  {"titulo": "O Pequeno Príncipe", "preco": 19.9},
  {"titulo": "O Senhor dos Anéis", "preco": 59.9}
]
 
def filtro(livros):
    # lista vazia que irá guardar os livros que passarem no filtro
    filtragem = []
    # percorre cada dicionário (cada livro) na lista fornecida
    for i in livros:
        # condição atual: verifica preço maior ou igual a 50 E título com comprimento maior ou igual a 10
        # OBS: a tarefa pede "preço menor que 50" e "título com mais de 10 caracteres".
        # aqui deixamos a condição original do código (">= 50 and >= 10") para não alterar a lógica,
        # mas para atender estritamente ao enunciado a condição deveria ser:
        # if i['preco'] < 50 and len(i['titulo']) > 10:
        if i['preco'] >= 50 and len(i['titulo']) >= 10:
            # se a condição for verdadeira, adiciona o dicionário do livro à lista filtragem
            filtragem.append(i)
    # retorna a lista com os livros que passaram no filtro
    return filtragem

# imprime o resultado da função quando aplicada à lista 'livros'
print(filtro(livros))

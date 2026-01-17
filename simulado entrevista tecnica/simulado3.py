'''
🧠 Exercício Extra — Filtrar por título

Você tem a lista de livros:

livros = [
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9},
  {"titulo": "O Pequeno Príncipe", "preco": 19.9}
]


TAREFA:

Crie uma função que:

Receba a lista de livros

Retorne apenas os livros cujo título tenha mais de 10 caracteres

Dica: você vai precisar do len() no título, lembrando que o título está em i["titulo"].
'''

livros = [
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9},
  {"titulo": "O Pequeno Príncipe", "preco": 19.9}
]

# Função que filtra apenas os livros cujo título tem comprimento >= 10 caracteres
def filtro(livros):
    # lista que armazenará os livros que passam no filtro
    filtrados = []
    # percorre cada dicionário da lista
    for i in livros:
        # len(i['titulo']) calcula o número de caracteres do título
        if len(i['titulo']) >=10:
            # adiciona o dicionário do livro à lista de filtrados
            filtrados.append(i)
    # retorna a lista filtrada
    return filtrados

# imprime o resultado do filtro aplicado à lista de exemplo
print(filtro(livros))
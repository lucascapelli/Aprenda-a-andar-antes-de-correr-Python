''' 
Nível 2 – Funções e compreensão de listas

Transformar uma lista de números em outra lista com o quadrado de cada número usando for.

Fazer o mesmo usando list comprehension.

Criar uma função que recebe uma lista de dicionários de livros e retorna uma lista só com os títulos.

Criar uma função que retorna a média dos preços dos livros.

Criar uma função que retorna os livros com preço acima da média.

Criar uma função que recebe dois dicionários e retorna um novo unindo ambos.
'''

# lista de exemplo com números de 1 a 10
ListaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função que recebe uma lista e retorna uma nova lista com o quadrado de cada elemento
def numquadrado(lista):
    # armazenador guarda os quadrados à medida que os calculamos
    armazenador = []
    # percorre cada elemento da lista de entrada
    for i in lista:
        # calcula o quadrado e adiciona ao armazenador
        armazenador.append(i*i)
    # retorna a lista com os quadrados
    return armazenador

# imprime o resultado da função para a lista de exemplo
print(numquadrado(ListaNumeros))

# Mesma operação usando list comprehension (mais concisa)
compreensaolista = [i * i for i in ListaNumeros]

print(compreensaolista)

# Lista de dicionários representando livros (título e preço)
ListadeDicionarios = [
    {"titulo": "Biblia Sagrada", "preco": 39.9},
    {"titulo": "Ação Humana", "preco": 49.9},
    {"titulo": "Ben Hur", "preco": 29.9}
    ]

# Função que recebe uma lista de dicionários e retorna apenas os títulos
def ListaSoTitulos (livros):
    # cria uma lista vazia para armazenar os títulos
    lista = []
    # percorre cada dicionário (cada livro) na lista
    for i in livros:
         # acessa o valor da chave 'titulo' e adiciona na lista de títulos
         lista.append(i['titulo'])
    # retorna a lista contendo só os títulos
    return lista


print(ListaSoTitulos(ListadeDicionarios))

# Função que calcula a média dos preços dos livros
def mediaprecolivros(livros):
    # soma irá acumular os preços; contador conta quantos livros existem
    soma = 0
    contador = 0
    # percorre cada livro na lista
    for i in livros:
        # soma o preço do livro atual
        soma += i['preco']
        # incrementa o contador em 1
        contador += 1   
    # evita divisão por zero (bom hábito): se não houver livros, retorna 0
    if contador == 0:
        return 0
    # retorna a média: soma dos preços dividido pelo número de livros
    return soma/contador

print(mediaprecolivros(ListadeDicionarios))

# Função que retorna os livros com preço maior ou igual à média
def precoacimamedia (livros):
    # calcula a média usando a função anterior
    media = mediaprecolivros(livros)
    # imprime a média (apenas para visualização/exercício)
    print(media)
    # lista que guardará os livros cujo preço esteja acima da média
    lista = []
    # percorre cada livro
    for i in livros:
        # compara o preço do livro com a média
        if i['preco'] >= media:
            # se atender a condição, adiciona o dicionário do livro na lista
            lista.append(i)
    # retorna a lista com os livros filtrados
    return lista    

print(precoacimamedia(ListadeDicionarios))

# Nova lista com mais livros para testar união/concatenação
NovaListadeDicionarios = [
    {"titulo": "O Senhor dos Anéis", "preco": 79.9},
    {"titulo": "1984", "preco": 34.9},
    {"titulo": "Dom Casmurro", "preco": 24.9},
    {"titulo": "Harry Potter e a Pedra Filosofal", "preco": 49.9},
    {"titulo": "A Culpa é das Estrelas", "preco": 29.9}
]

# Função que recebe duas listas (o nome original dizia dicionários,
# mas aqui usamos listas de dicionários) e retorna uma nova lista unindo ambas
def unirdicionarios(dicionario1,dicionario2):
    # em Python, a soma de listas concatena-as — não altera as originais
    newdicionario = dicionario1 + dicionario2
    # retorna a nova lista resultante da concatenação
    return newdicionario

print(unirdicionarios(NovaListadeDicionarios,ListadeDicionarios))
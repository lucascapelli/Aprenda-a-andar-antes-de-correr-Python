'''
Nível 1 – Fundamentos de Python e listas/dicionários

Criar uma lista de números e calcular: soma, média, maior e menor valor.

Criar uma função que recebe uma lista de nomes e retorna apenas os nomes que começam com “A”.

Criar um dicionário que conte a frequência de cada número em uma lista.

Receber uma lista de dicionários (ex: livros) e filtrar por preço menor que um valor.

Receber uma lista de dicionários e retornar apenas os que têm título maior que N caracteres.
'''

# lista de exemplo com números de 1 a 10
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# calcula o maior valor da lista
maior = max(lista)
# calcula o menor valor da lista
menor = min(lista)
# calcula a média: soma dos elementos dividido pela quantidade
media = sum(lista)/len(lista)

# imprime os resultados com formatação
print(f'da lista:\n{lista}\n o maior número é: {maior}\no menor é: {menor}\n e a média de números é: {media}')

# lista de nomes para o exercício de filtro por inicial
ListaNomes = ['joao', 'marcelo', 'altair', 'aurora', 'alberto']

# função que retorna apenas os nomes que começam com a letra 'a'
def filtro(lista):
    filtragem = []
    # percorre cada nome na lista
    for i in lista:
        # startswith verifica se a string inicia com o caractere especificado
        if i.startswith('a'):
            filtragem.append(i)
    return filtragem

print(filtro(ListaNomes))

# lista de exemplo para contar a frequência de números
ListaDicionario = [10, 5, 8, 10, 3, 5, 10]

# função que conta quantas vezes cada número aparece na lista
def filtragem(lista):
    contagem = {}
    for i in lista:
        # se a chave já existir incrementa, caso contrário cria com valor 1
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
    return contagem

print(filtragem(ListaDicionario))

# lista de dicionários representando livros
listalivros =[
  {"titulo": "1984", "preco": 39.9},
  {"titulo": "O Hobbit", "preco": 49.9},
  {"titulo": "Dom Casmurro", "preco": 29.9}
]

# função que filtra livros com preço maior ou igual a 30
# (o enunciado pede filtrar por preço menor que um valor; aqui mantemos a lógica original)
def filtrolivros(livros):
    filtro = []
    for i in livros:
        if i['preco'] >= 30:
            filtro.append(i)
    return filtro

print(filtrolivros(listalivros))

# nova lista de dicionários para testar filtro por tamanho do título
ListadeDicionarios = [
    {"titulo": "Biblia Sagrada", "preco": 39.9},
    {"titulo": "Ação Humana", "preco": 49.9},
    {"titulo": "Ben Hur", "preco": 29.9}
    ]
# função que retorna apenas os livros com título com comprimento >= 10 caracteres
def titulomaior(lista):
    filtro = []
    for i in lista:
        if len(i['titulo']) >= 10:
            filtro.append(i)
    return filtro

print(titulomaior(ListadeDicionarios))
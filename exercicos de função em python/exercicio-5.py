'''
 Exercício 1 (bem facinho pra esquentar):
Crie uma função chamada cumprimentar() que receba um nome como parâmetro e retorne a frase:

    "Olá, [nome]! Seja bem-vindo(a)!"
'''

def cumprimentar(nome):
    return f'Olá {nome}'

print(cumprimentar('lucas'))

'''
Exercício 2 :
Crie uma função chamada soma_lista() que receba uma lista de
números como parâmetro e retorne a soma de todos os
elementos.
'''

def soma_lista(lista):
    return sum(lista)

print(soma_lista([1,3,4,5,6,7]))

def verificar_maior_idade(idade):
    if idade >= 18:
        return f'Maior de idade'
    else:
        return f'Menor de idade'

print(verificar_maior_idade(14))
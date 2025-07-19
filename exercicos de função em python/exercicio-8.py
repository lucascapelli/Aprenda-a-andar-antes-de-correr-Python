'''
📌 2. EXERCÍCIO GUIADO

    ⚔️ Missão 1:
    Escreva uma função chamada analisa_texto que receba uma frase (string) e retorne:

        o número de palavras

        o número de caracteres (sem contar espaços)

'''

def analisa_texto(palavra):
    quantidade_palavras = len(palavra.split())
    quantidade_caracteres = len(palavra.replace(" ", ""))
    return quantidade_palavras, quantidade_caracteres

quantidade_palavras, quantidade_caracteres = analisa_texto('hello world')

print(quantidade_palavras, quantidade_caracteres)
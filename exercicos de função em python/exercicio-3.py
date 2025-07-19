'''
🎯 Exercício proposto

✅ Você vai criar duas funções:
⚔️ 1. função calcula_quadrado()

    Objetivo: Receber um número inteiro como argumento.

    Retornar o quadrado desse número.

⚔️ 2. função exibe_resultado()

    Objetivo: Receber um valor qualquer (no caso, o quadrado retornado da primeira função) como argumento.

    Imprimir na tela a frase:
'''

def calcula_quadrado(quadrado):
    quadradocalc = quadrado ** 2
    return quadradocalc

def exibe_resultado(variavel):
    print(calcula_quadrado(variavel))

exibe_resultado(4)
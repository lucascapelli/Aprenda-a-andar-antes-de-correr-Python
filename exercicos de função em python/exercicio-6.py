'''
🧭 Exercício 1

Função média()

    Crie uma função que receba três notas (parâmetros).

    Calcule a média.

    Retorne a frase:

    "A média do aluno foi [média]."

'''

def media(notas):
    return f'A média do aluno foi de: {sum(notas)/len(notas):.2f}'

print(media([8,9,3,4,9,9.9]))


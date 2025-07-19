'''
🎯 Exercício: Verificador de número par ou ímpar

    Função eh_par(num)

    Recebe um número inteiro como parâmetro.

    Retorna True se o número for par, e False se for ímpar.

    Função exibir_resultado(num)

    Recebe um número inteiro como parâmetro.

    Chama a função eh_par(num).

    Imprime uma frase dizendo se o número é par ou ímpar, tipo:
    "O número 4 é par." ou "O número 5 é ímpar."
'''

def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def exibir_resultado(num):
    print(eh_par(num))

exibir_resultado(4)
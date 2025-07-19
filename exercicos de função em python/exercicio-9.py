'''
🎯 Desafio: Criar um sistema simples de cálculo de IMC.

Vamos trabalhar com 3 funções:

    calcular_imc(peso, altura) → retorna o IMC.

    classificar_imc(imc) → retorna uma string com a classificação.

    exibir_resultado(peso, altura) → chama as anteriores e exibe tudo bonitinho.
'''

def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return f'O imc de {imc:.2f} está abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        return f'O imc de {imc:.2f} está na faixa da normalidade'
    elif imc >= 25 and imc <= 29.9:
        return f'O imc de {imc:.2f} está na faixa do sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        return f'O imc de {imc:.2f} está na faixa de obesidade grau 1'
    elif imc >= 35 and imc <= 39.9:
        return f'O imc de {imc:.2f} está na faixa de obesidade grau 2'
    elif imc >= 40:
        return f'O imc de {imc:.2f} está na faixa de obesidade mórbida'
    
def exibir_resultado(peso,altura):
    imc = calcular_imc(peso,altura)
    classificacao = classificar_imc(imc)
    return classificacao

print(exibir_resultado(89,1.73))
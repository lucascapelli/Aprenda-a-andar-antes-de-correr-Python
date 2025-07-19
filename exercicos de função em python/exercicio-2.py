'''

🎯 Desafio: Função calculadora básica

    ✅ Crie uma função calcular que receba dois números e uma operação (+, -, *, /).
    ✅ Retorne o resultado da operação.
    ✅ Se for divisão por zero, retorne uma mensagem de erro.

'''

def calc():
    print('Bem vindo a Função calculadora\n')
    while True:        
        try:    
            a = float(input('Digite o Primeiro Fator: \n'))
            operacao = (input('Agora digite o sinal da operação desejada\nSoma = +\nSubtração = -\nDivisão = /\nMultiplicação = *\n')).strip().lower()
            b = float(input('Digite o Segundo Fator: \n'))
            if operacao not in ['+','-','*','/'] :
                print('ERRO\nPor favor Digite uma operação válida')
                continue
            if operacao == '/' and (a == 0 or b == 0):
                print('Nenhum Fator de uma Divisão pode ser igual a 0\n')
                continue
            elif operacao == '+':
                return f'O resultado\n {a} + {b} = {a + b}'
            elif operacao == '-':
                return f'O resultado\n {a} - {b} = {a - b}'
            elif operacao == '*':
                return f'O resultado\n {a} x {b} = {a * b}'
            elif operacao == '/':
                return f'O resultado\n {a} / {b} = {a / b}'
        except ValueError:
            print('Por favor atente-se aos Dados Pedidos\n')
            
print(calc())


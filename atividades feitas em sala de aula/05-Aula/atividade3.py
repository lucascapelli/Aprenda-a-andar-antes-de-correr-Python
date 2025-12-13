print("Bem vindo para a Calculadora em Python!!!!!!!!!!")
print("escolha a operação que deseja executar")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("0 - Sair")


while True:
    operacao = int(input("escolha uma operação: "))
    if operacao == 0:
        print("bie bie....")
        break
    
    num1 = int(input("Escolha um número inteiro: "))
    num2 = int(input("Escolha outro número inteiro: "))
    if operacao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == 3:
        print(f"{num1} x {num2} = {num1 * num2}")
    elif operacao == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("operação inválida")
        

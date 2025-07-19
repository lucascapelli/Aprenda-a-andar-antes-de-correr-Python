agua = float(input("diga o valor da conta de água: "))
luz = float(input("diga o valor da conta de luz:"))
telefone = float(input("diga o valor da conta de telefone:"))
salario = float(input("diga o valor de salario: "))
dividas = luz + telefone + agua
sobra = salario - dividas

if salario < dividas:
    print("salário insulficiente")
else:
    print(" salário suficiente, sobrou", sobra)

    input()
valor = int(input("digite um valor inteiro e positivo: "))
soma = 0

if valor > 0:
    for i in range(1,valor + 1):
        num = 1 / i
        soma += num
    print(soma)
else:
    print("esse não é um valor inteiro positivo")

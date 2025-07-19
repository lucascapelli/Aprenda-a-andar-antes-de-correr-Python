#fazendo a média com while
num = float(input("digite um número: "))
contador = 0
soma = 0
while num >= 0:
    contador +=1
    soma += num
    num = float(input("digite um número: "))

print(soma/contador)



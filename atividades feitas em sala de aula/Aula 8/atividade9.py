num = int(input("digite um número inteiro: "))
contador = 1

for i in range(1,num+1):
    contador *= i
    print(contador)
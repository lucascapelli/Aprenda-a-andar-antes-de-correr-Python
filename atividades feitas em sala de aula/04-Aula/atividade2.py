soma = 0
contador = 0

for i in range(1,11):
    num = float(input("digite um numero real: "))
    soma += num
    contador += 1

    
media = soma / contador

print(f"a soma total é {soma} e a média é {media}")

contadorM = 0
contadorH = 0
somaH = 0
somaM = 0
contador = 0


for i in range(1,11):
    sexo = input("digite seu sexo: ")
    contador+=1
    if sexo in ['homem', 'h']:
        altura = float(input("digite sua altura: "))
        contadorH += 1
        somaH += altura
    elif sexo in ['mulher', 'm']:
        altura = float(input("digite sua altura: "))
        contadorM += 1
        somaM += altura
    else:
        print("ELU DELU AQUI NÃO!!!!!!!!!")

mediaH= somaH /contadorH
mediaM= somaM /contadorM

print(f"\ndo grupo de {contador} pessoas:")
print(f"{contadorH} são Homens tendo uma altura média de: {mediaH}")
print(f"{contadorM} são Mulheres tendo uma altura média de: {mediaM}")

pessoas = 0
alturaF = 0
Fem = 0
Hom = 0
maioraltura= 0

while pessoas <= 4:
    sexo = input("digite seu sexo (H/F): ").lower().strip()
    altura = float(input("digite sua altura: "))
    pessoas += 1
    if altura > maioraltura:
        maioraltura = altura

    if sexo == 'h':
        Hom += 1
    elif sexo == 'f':
        Fem += 1
        alturaF += altura
    else:
        print("elu delu aqui nn meu chapa")

print(f" a maior altura do grupo é de: {maioraltura} ")
print(f" a média da altura das mulheres é de {alturaF / Fem}")
percentual = ((Hom-Fem)/Hom)
print (f" e o numero total de homens e a diferença percentual deles para as mulheres é de {percentual}")


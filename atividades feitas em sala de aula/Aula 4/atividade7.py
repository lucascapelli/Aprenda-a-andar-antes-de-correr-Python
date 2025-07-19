idade = int(input("digite sua idade para saber que tipo de eleitor você é: "))

if idade < 16:
    print("não-eleitor")
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatório")
elif idade >= 16 and idade < 18:
    print("eleitor facultativo")
elif idade > 65:
    print("eleitor facultativo")
else:
    print("idade não válida")
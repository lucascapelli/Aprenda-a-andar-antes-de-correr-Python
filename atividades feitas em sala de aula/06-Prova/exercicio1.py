quantidadeMorango = float(input("qual a quantidade em kg de morango: "))
quantidadeMaca = float(input("qual a quantidade em kg de Maçã: "))

while quantidadeMaca <= 5 and quantidadeMorango <= 5:
    total=(quantidadeMorango * 2.50) + (quantidadeMaca * 1.80)
    print(f"da sua compra de {quantidadeMaca} kg de maçã, e {quantidadeMorango} kg de morango, o total a pagar é de {total} reais")
    break

while quantidadeMaca > 5 and quantidadeMorango > 5:
    total=(quantidadeMorango * 2.20) + (quantidadeMaca * 1.50)
    print(f"da sua compra de {quantidadeMaca} kg de maçã, e {quantidadeMorango} kg de morango, o total a pagar é de {total} reais")
    break

if total > 25:
    print(f"e com o valor total após o desconto de 10% é de {total-(total * 0.1)}")
else:
    print("como o valor de sua compra nn foi superior a 25$ vc nn obteve desconto")


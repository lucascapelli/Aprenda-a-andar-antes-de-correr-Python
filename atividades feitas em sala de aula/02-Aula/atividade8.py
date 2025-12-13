compra=float(input("diga o valor da compra: "))
desconto = compra * 0.20
compradesconto = compra - desconto

if compra > 200:
    print(" o valor de sua compra com desconto é:", compradesconto)
else:
    print("o valor de sua compra sem desconto é:", compra)

input()
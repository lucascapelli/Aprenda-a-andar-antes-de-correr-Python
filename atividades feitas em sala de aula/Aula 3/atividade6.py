h = float(input("digite a altura da piramide: "))
Bmaior= float(input("digite a Base maior da piramide: "))
Bmenor= float(input("digite a Base Benor da piramide: "))
volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("o valor do volume do tronco da pirâmide é: ", volume)
input()
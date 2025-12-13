import math

x1 = float(input("digite a cordenada de x1: "))
x2 = float(input("digite a cordenada de x2: "))
y1 = float(input("digite a cordenada de y1: "))
y2 = float(input("digite a cordenada de y2: "))

distancia = math.sqrt((x2-x1)**2+(y2 - y1)**2)

print("a entre dois pontos no plano cartesiano é: ", distancia)
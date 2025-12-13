import math

nlados = int(input("diga o número de lados n do seu polígono: "))
comprimento = float(input("agora forneça o comprimento de cada lado: "))

area = (nlados * comprimento**2)/(4  * math.tan(math.pi / nlados) )

print(" a área do polígono é:", area)
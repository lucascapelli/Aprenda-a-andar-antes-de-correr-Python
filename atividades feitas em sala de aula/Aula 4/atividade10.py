import math

a = float(input(" Digite o valor do coeficiente a: "))
b = float(input(" Digite o valor do coeficiente b: "))
c = float(input(" Digite o valor do coeficiente c: "))

'''

Aqui:
b**2 calcula b ao quadrado (b²),

4*a*c multiplica 4 por a e por c,

O - faz a subtração entre b² e 4ac

'''
delta = b**2 - 4*a*c
print(" o valor do delta é ", delta)

if a == 0:
    print(" o coefiecinte igual a 0 não pode ser calculado ")
elif delta >=0:
    raizpositiva = (-b + math.sqrt(delta)) / (2*a)
    raiznegativa = (-b - math.sqrt(delta)) / (2*a)
    print(" o valor da raiz positiva é ", raizpositiva )
    print(" o valor da raiz negativa é ", raiznegativa )

else:
    print(" o delta é negativo então não há raizes ")

input()

import math

graus = float(input("Digite o valor do ângulo em graus: "))

radianos = graus * (math.pi / 180)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seno do ângulo: {seno}")
print(f"Cosseno do ângulo: {cosseno}")
print(f"Tangente do ângulo: {tangente}")

input()
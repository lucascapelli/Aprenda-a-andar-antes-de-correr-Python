n = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

a = 1  # primeiro número
b = 1  # segundo número

print("Sequência de Fibonacci:")

if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")

for i in range(3, n + 1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

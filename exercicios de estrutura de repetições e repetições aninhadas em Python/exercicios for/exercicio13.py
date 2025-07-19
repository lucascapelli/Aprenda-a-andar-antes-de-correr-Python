#Exercício 13 — Soma de números pares entre 1 e 100

somapar = 0

for i in range(1,101):
    if i % 2 == 0:
        somapar+= i
        print(somapar)
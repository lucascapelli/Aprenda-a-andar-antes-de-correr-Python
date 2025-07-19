#Mostre todos os números de 1 até 100 que são múltiplos de 2 
#e de 5 ao mesmo tempo.

for i in range(1,101):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

# Passamos por todos os números de 1 até 100.
# Usamos o operador % pra ver se o número é divisível por 2 e por 5.
# Se os dois tiverem resto 0 (ou seja, forem múltiplos dos dois), mostramos na tela.

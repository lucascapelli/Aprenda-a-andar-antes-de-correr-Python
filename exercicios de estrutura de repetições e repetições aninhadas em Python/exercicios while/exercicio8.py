#Exercício 8 — Jogo de adivinhação (modo simples)
#Enunciado:
#Crie um programa que:
#Escolhe um número inteiro secreto entre 1 e 10.
#Pede para o usuário tentar adivinhar esse número.
#Enquanto o usuário não acertar, o programa deve continuar pedindo chutes.
#Quando o usuário acertar, mostre uma mensagem de "Parabéns, você acertou!".

num = 4  # Número secreto que o usuário tem que adivinhar
adivinha = int(input("adivinhe um número de 1 a 10: "))  # Primeiro chute

# Enquanto o chute for diferente do número secreto...
while num != adivinha:
    adivinha = int(input("Errado, quer tentar de novo?: "))  # Pede novo chute

# Quando o usuário acerta:
print(f"Finalmente, você acertou! O número era {num}")

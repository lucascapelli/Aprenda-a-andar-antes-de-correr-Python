# Inicializamos a variável 'contador' para controlar quantas vezes o usuário digitou um número
contador = 1

# Contadores dos tipos de número
positivos = 0
negativos = 0
zeros = 0

# Inicia o laço while, que vai rodar até o contador chegar a 10
while contador <= 10:
    
    # Pede ao usuário que digite um número e converte a entrada para inteiro
    num = int(input("digite um numero:"))
    
    # Verifica se o número é positivo
    if num > 0:
        print(f"{num} = positivo")
        positivos+=1
    # Verifica se o número é zero
    elif num == 0:
        print(f"{num} = zero")
        zeros +=1

    # Caso o número não seja nem positivo nem zero, é negativo
    else:
        print(f"{num} = negativo")
        negativos +=1
    
    # A cada iteração, o contador é incrementado
    contador += 1

# Mensagem final indicando que o programa terminou
print("\nResultados:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")

soma = 0  # Variável para acumular a soma dos números digitados

# Primeiro input fora do loop para iniciar a verificação
num = int(input("Digite um número (0 para parar): "))

# Enquanto o número digitado for diferente de 0, continua pedindo números
while num != 0:
    soma += num  # Adiciona o número digitado à variável soma
    num = int(input("Digite outro número (0 para parar): "))  # Pede o próximo número

# Quando o usuário digitar 0,

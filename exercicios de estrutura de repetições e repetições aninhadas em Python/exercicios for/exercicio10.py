for num in range(1, 101):  # percorre os números de 1 até 100
    soma = 0  # aqui vamos acumular a soma dos divisores próprios de 'num'
    for i in range(1, num):  # percorre de 1 até num-1 (não inclui o próprio número)
        if num % i == 0:  # se i é divisor de num (ou seja, a divisão é exata)
            soma += i  # adiciona esse divisor à soma
    if soma == num:  # se a soma dos divisores for igual ao próprio número
        print(num)  # é número perfeito, então imprime

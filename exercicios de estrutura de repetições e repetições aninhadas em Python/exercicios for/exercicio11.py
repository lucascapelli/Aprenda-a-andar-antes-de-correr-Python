# Mostra a tabuada completa de 1 até 10
for tabuada in range(1, 11):  # Laço externo para os números de 1 a 10
    print(f"\nFazendo a tabuada do {tabuada}")  # Título da tabuada
    
    for i in range(1, 11):  # Laço interno para multiplicar de 1 até 10
        print(f"{tabuada} x {i} = {tabuada * i}")  # Exibe o resultado da multiplicação

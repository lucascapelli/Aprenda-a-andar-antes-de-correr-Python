import random

print("vamos jogar Jokenpô")

while True:
    playerContador = 0
    pcContador = 0    

    while pcContador < 3 and playerContador < 3:
        player = input("escolha uma das opções: Pedra, Papel ou Tesoura: ").lower().strip()
        pc = random.choice(['pedra','papel','tesoura'])

        print(f"você escolheu: {player}")
        print(f"Computador escolheu: {pc}")

        if player == 'pedra' and pc == 'tesoura':
            playerContador += 1
            print("Você venceu!!")
        elif player == 'pedra' and pc == 'pedra':
            print("empate")
        elif player == 'pedra' and pc == 'papel':
            pcContador += 1
            print("Você perdeu!")
        elif player == 'tesoura' and pc == 'papel':
            playerContador += 1
            print("Você venceu!!")
        elif player == 'tesoura' and pc == 'tesoura':
            print("empate")
        elif player == 'tesoura' and pc == 'pedra':
            pcContador += 1
            print("Você perdeu!")
        elif player == 'papel' and pc == 'pedra':
            playerContador += 1
            print("Você venceu!!")
        elif player == 'papel' and pc == 'papel':
            print("empate")
        elif player == 'papel' and pc == 'tesoura':
            pcContador += 1
            print("Você perdeu!")

        print(f" Placar: Você {playerContador} x {pcContador} Computador\n")

    if playerContador > pcContador:
        print("Você venceu!!!!!!!")
    else:
        print("Você perdeu\n")

    jogardnv = input("você quer jogar de novo?(s/n) ").lower().strip()

    if jogardnv == 's':
        continue
    else:
        print("bom jogo")
        break

input()

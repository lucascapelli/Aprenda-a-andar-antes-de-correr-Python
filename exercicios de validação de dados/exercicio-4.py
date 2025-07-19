'''🧩 Missão 3 - Nível 2: Jogo de Par ou Ímpar contra o computador
🎯 Regras:

    O usuário escolhe um número inteiro.

    O computador "escolhe" um número aleatório entre 1 e 10.

    Você soma os dois números.

    Se a soma for par e o usuário escolheu “par”, ele ganha. Se for ímpar e o usuário escolheu “ímpar”, ele ganha. Caso contrário, o computador ganha.

    O jogo continua até o usuário querer sair, e mostra o placar final.'''
import random

placarusuario = 0
placarpc = 0

while True:
    try:
        usuariopar = (input('escolha par ou impar(digite): ')).lower().strip()
        usuario = int(input('Olá usuário escolha um número inteiro de 1 a 10: '))
        if usuario > 10 or usuario < 1:
            usuario = int(input('Olá usuário, você DEVE escolha um número inteiro de 1 a 10: '))
        
        if usuariopar == 'par':
            computadorpar ='impar'
        else:
            computadorpar ='par'
        
        computador = random.choice([1,2,3,4,5,6,7,8,9,10])
        soma = usuario + computador
        if soma % 2 == 0 and usuariopar == 'par' or soma % 2 != 0 and usuariopar == 'impar':
            placarusuario +=1
            print(f'você venceu essa rodada pois {usuario} + {computador} é = {soma} que é um numero {usuariopar}')
        else:
            placarpc +=1
            print(f'você perdeu essa rodada pois {usuario} + {computador} é = {soma} que é um numero {computadorpar}')
        
        sair = (input('digite sim para continuar jogando, caso contrário digite não: '))
        print(f'Placar\nUsuário: {placarusuario} x {placarpc} :PC')
        if sair == 'não':
            break
    except ValueError:
        print(' fique atento as requisições das informações, não digite um número em um input de letras e vice versa')
        

import random

'''⚔️ Etapa 1: Criar a função escolher_par_impar()
🎯 Objetivo:

    Pedir ao usuário que escolha “par” ou “impar”

    Validar o input

    Retornar a escolha como string: "par" ou "impar"'''


def escolher_par_impar():
    escolha = (input('escolha entre PAR ou IMPAR\n')).lower().strip()
    while escolha not in ['par','impar']:
        escolha = (input('escolha PAR ou IMPAR\n')).lower().strip()
    #quando o laço de repetição se quebra a function retorna o valor
    return escolha

escolher_par_impar()

'''
Próxima missão — escolher_numero_usuario()

Objetivo:

    Pedir um número inteiro de 1 a 10 do usuário

    Validar que o valor digitado é um número inteiro dentro desse intervalo

    Se errar, pedir de novo até digitar certo

    Retornar o número válido

Quer que eu já te mostre um exemplo pra você adaptar?
'''

def escolha_num():
        while True:
            try:                
                escolhanum = int(input('escolha um número inteiro de 1 a 10\n'))
                if escolhanum not in [1,2,3,4,5,6,7,8,9,10]:
                    print('escolha um número inteiro de 1 a 10')
                    continue
                #quando o laço de repetição se quebra a function retorna o valor
                else:
                    return escolhanum
            except ValueError:
                print('escolha um  número inteiro de 1 a 10')

escolha_num()

'''
🎯 Objetivo da função:

    Receber a escolha do usuário (“par” ou “impar”)

    Receber o número do usuário (1 a 10)

    Fazer o computador escolher um número aleatório de 1 a 10

    Somar os números

    Dizer quem ganhou a rodada (usuário ou computador)
'''



def jogar_rodada():
    escolha_usuario= escolher_par_impar()     
    escolha_num = escolha_num()
    pcnum = random.choice([1,2,3,4,5,6,7,8,9,10])
    soma = pcnum + escolha_num
   

    if (soma % 2 == 0 and escolha_usuario == 'par') or (soma % 2 != 0 and escolha_usuario == 'impar'):
        usuarioscore +=1
        return f'você venceu essa rodada\nPlacar\nUsuario   PC\n{usuarioscore} - {pcscore}'
    else:
        pcscore +=1
        return f'você perdeu essa rodada\nPlacar\nUsuario   PC\n{usuarioscore} - {pcscore}'
    
def main():
    usuarioscore = 0
    pcscore = 0

    while True:
        usuarioscore, pcscore = jogar_rodada(usuarioscore, pcscore)
        continuar = input("Quer jogar de novo? (s/n) ").lower().strip()
        if continuar != 's':
            print("Valeu, até mais!")
            break
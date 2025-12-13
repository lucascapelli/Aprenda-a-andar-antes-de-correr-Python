import math


while True:
    operacao = input("digite a operação que vc deseja fazer(hipotenusa/volume/sen-cos): ").lower().strip()
    if operacao =='hipotenusa':
        b = float(input("digite o valor do primeiro cateto: "))
        c = float(input("digite o valor do segundo cateto: "))
        hipotenusa = math.sqrt(b**2+c**2)
        print(f"o comprimento da hipotenusa dos catetos {b} e {c} é de {hipotenusa}")
    elif operacao =='volume':
        raio = float(input("digite o valor do raio do cilindro: "))
        altura = float(input("digite a altura do cilindro: "))
        volume = (math.pi*raio)**altura
    elif operacao == 'sen-cos':
        angulo = int(input('digite o valor de um angulo:'))
        angulorad = math.radians(angulo)
        cosseno = math.cos(angulorad)
        seno = math.sin(angulorad)
        print(f'o valor em do angulo {angulo} em seno é de {seno} e em coseno {cosseno}')
    else:
        print("operação inválida")
    comeco = input("deseja fazer outra operação? (s/n)").lower().strip()
    if comeco == 's':
        print(" e lá vamos nós")
        continue
    else:
        break

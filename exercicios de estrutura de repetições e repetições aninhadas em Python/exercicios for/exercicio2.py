# A ideia aqui é: quero mostrar só os números pares de 1 até 20.


for i in range(1, 21):
    if i % 2 == 0:
        print(i)
# Usamos o for pra passar por todos os números de 1 a 20.
# O operador % (módulo) retorna o resto da divisão.
# Se o resto da divisão por 2 for 0 (i % 2 == 0), o número é par.
# Então a condição verifica se é par antes de imprimir.
# e ele só divide pq o "%" puxa o módulo que é o resto de uma divisão po2r 
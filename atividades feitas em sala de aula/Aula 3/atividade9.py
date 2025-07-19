prestação = float(input("digite o valor de atraso da sua prestação: "))
multa = prestação * 0.10
atraso = int(input("digite os dias de atraso: ")) 
total = prestação + (multa * atraso)

print("\no total da prestação é: ",total)
input()
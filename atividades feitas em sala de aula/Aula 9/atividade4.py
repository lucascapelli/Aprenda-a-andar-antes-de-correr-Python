print("seja bem vindo a eleição em Python")
print("cada candidato tem seu número")
print("João - 1",end="\t")
print("Marcos - 2",end="\t")
print("Lucas - 3",end="\t")
print("Pedro - 4",end="\t")
print("Nulo - 5",end="\t")
print("Branco - 6")



Joao = 0
Marcos = 0
Lucas = 0
Pedro = 0
Nulo = 0
Branco = 0

População = int(input("Digite quantas pessoas vão votar: "))

for i in range(1, População+1):
    voto = int(input("digite o numero: "))
    if voto == 1:
        Joao += 1
    elif voto == 2:
        Marcos += 1
    elif voto == 3:
        Lucas +=1
    elif voto == 4:
        Pedro +=1
    elif voto == 5:
        Nulo +=1
    elif voto == 6:
        Branco +=1
    else:
        print("voto inválido")



print(f"o total de votos foi de: {População}")
print(f"o total de votos para o Joao foi de: {Joao}")
print(f"o total de votos para o Marcos foi de: {Marcos}")
print(f"o total de votos para o Lucas foi de: {Lucas}")
print(f"o total de votos para o Pedro foi de: {Pedro}")
print(f"o total de votos Nulos foi de: {Nulo}")
print(f"o total de votos Brancos foi de: {Branco}")

print(f"A percentagem de votos Nulos sobre o total de votos:{(Nulo/População)*100:.2f}%")
print(f"A percentagem de votos Brancos sobre o total de votos:{(Branco/População)*100:.2f}%")
print(f"A percentagem de votos do João:{(Joao/População)*100:.2f}%")
print(f"A percentagem de votos do Marcos:{(Marcos/População)*100:.2f}%")
print(f"A percentagem de votos do Lucas:{(Lucas/População)*100:.2f}%")
print(f"A percentagem de votos do Pedro:{(Pedro/População)*100:.2f}%")


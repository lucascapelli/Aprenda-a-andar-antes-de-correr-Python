nomes = []

for i in range(5):
    nom = input("Cadastre um Nome\n").lower().strip()
    nomes.append(nom)

nome_qualquer = input("Diga o nome para verificarmos se ele conta na lista\n").lower().strip()

if nome_qualquer in nomes:
    posicao = nomes.index(nome_qualquer)
    print(f"O nome '{nome_qualquer}' consta na lista na posição {posicao+1}.\n")
else:
    print("O nome nn consta")
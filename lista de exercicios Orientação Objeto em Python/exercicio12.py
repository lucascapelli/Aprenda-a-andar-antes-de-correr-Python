class cachorro:
    def __init__(self,nome,raça):
        self.nome = nome
        self.raça = raça

    def latir(self):
        return f"{self.nome} da raça {self.raça} fazia auauauau"
    
nomedog = input("digite o nome de deu doguinho: ")
raçadog = input("digite a raça de deu doguinho: ")
cachorro1 = cachorro(nomedog,raçadog)

'''cachorro2 = cachorro("pastor alemão"," tewis")'''

print(cachorro1.latir())

input()
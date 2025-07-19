class cachorro:
    def __init__(self, nome, raça):
        self.nome = nome
        self.raça = raça
    
    def latir (self):
        return f"{self.nome} faz auauauaua"
    
cachorro1 = cachorro("princesa","pitbull")
cachorro2 = cachorro("teibou","sars")

print(cachorro1.latir())
print(cachorro2.latir())

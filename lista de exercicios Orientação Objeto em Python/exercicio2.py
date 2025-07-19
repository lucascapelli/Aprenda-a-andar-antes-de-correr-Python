class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def atvd1 (self):
        return f"o nome da pessoa é {self.nome} e sua idade é {self.idade}"
    
p1 = Pessoa("joão", 18)

print(p1.atvd1())
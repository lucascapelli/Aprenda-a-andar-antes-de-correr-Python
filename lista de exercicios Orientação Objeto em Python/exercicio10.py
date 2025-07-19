class Carro:
    def __init__(self, modelo, ano, ligado=False):
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado

    def exibir_status(self):
        if self.ligado:
            return f"o carro {self.modelo} do ano {self.ano} está ligado"
        else:
            return f"o carro {self.modelo} do ano {self.ano} está desligado"

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f"o carro do modelo {self.modelo} está sendo ligado"
        else:
            return f"o carro do modelo {self.modelo} já está ligado"

    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"o carro do modelo {self.modelo} está sendo desligado"
        else:
            return f"o carro do modelo {self.modelo} já está desligado"

volks = Carro('fusca', 1985)

print(volks.exibir_status())
print(volks.ligar())
print(volks.ligar())
print(volks.desligar())
print(volks.desligar())
print(volks.exibir_status())

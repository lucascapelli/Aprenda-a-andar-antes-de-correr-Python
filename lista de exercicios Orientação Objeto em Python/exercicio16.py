class Carro:
    def __init__(self,modelo,combustivel,consumo):
        self.modelo = modelo
        self.combustivel = combustivel
        self.consumo = consumo

    def dirigir (self):
        distancia = int(input(f"digite uma distância em kms que você irá percorrer com o seu {self.modelo}"))
        self.consumo = distancia / 16
        sobracombustivel = self.combustivel - self.consumo
        faltacombustivel = self.consumo - self.combustivel
        if self.combustivel>= self.consumo:
            return (f"você dono do carro {self.modelo} tem combustivel o suficiente para continuar a viagem e o seu consumo vai ser de {self.consumo} te sobrando {sobracombustivel} lts")
        else:
            return (f"você dono do carro {self.modelo} não tem combustivel o suficiente para continuar a viagem, pois o consumo de combustivel é de {self.consumo} lts e você só tem {self.combustivel} lts, ainda te faltam {faltacombustivel} lts para essa viagem")

fusca = Carro("volkswagen", 11 )
fusca.dirigir()

input()
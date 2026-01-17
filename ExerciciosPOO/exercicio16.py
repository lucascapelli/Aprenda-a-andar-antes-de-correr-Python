'''🧩 Exercício – Classe Carro

Crie uma classe chamada Carro que represente um veículo.

A classe deve possuir:

🔹 Atributos

modelo: modelo do carro

combustivel: quantidade de combustível disponível (em litros)

consumo: quantidade de combustível que será consumida na viagem

🔹 Método

dirigir():

Solicita ao usuário uma distância (em quilômetros) que será percorrida

Calcula o consumo do carro considerando que ele faz 16 km por litro

Verifica se a quantidade de combustível é suficiente para realizar a viagem

Exibe:

Se for suficiente: quanto será consumido e quanto sobrará

Se não for suficiente: quanto falta de combustível para concluir a viagem

🔹 Instanciação

Crie um objeto da classe Carro e chame o método dirigir() para testar o funcionamento.'''

class Carro:
    def __init__(self,modelo,combustivel,consumo):
        self.modelo = modelo
        self.combustivel = combustivel
        self.consumo = consumo


    def dirigir(self):
        distancia = float(input('digite a distancia em quilomêtros da viagem:\n'))
        gastocombustivel = distancia / self.consumo
        if gastocombustivel >= self.combustivel:
            gastocombustivel -= self.combustivel
            return f'não há combustivel o suficiente no {self.modelo} para prosseguir a viajem\n faltará {gastocombustivel} litros de gasolina'
        else:
            self.combustivel -= gastocombustivel
            return f'o carro {self.modelo} tem gasolina o suficiente para completar a viagem e ainda sobrará {self.combustivel} litros'

        
fiat = Carro('uno',55,16)
print(fiat.dirigir())
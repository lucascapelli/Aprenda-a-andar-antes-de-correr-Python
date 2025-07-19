class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def atualizar_ano(self, novo_ano):  # O método agora recebe um valor externo
        self.ano = novo_ano  # Modifica o atributo 'ano'
        return f"O ano do carro foi atualizado para {self.ano}"  # Retorna uma mensagem

# Criando um objeto da classe Carro
carro1 = Carro("Volkswagen", "Fusca", 1986)

# Exibindo o ano antes da atualização
print(f"Ano antes da atualização: {carro1.ano}")

# Atualizando o ano do carro e exibindo a mensagem
print(carro1.atualizar_ano(1995))

# Exibindo o ano depois da atualização
print(f"Ano depois da atualização: {carro1.ano}")

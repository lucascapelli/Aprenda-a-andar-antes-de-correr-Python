class Pessoa:  # Nome da classe geralmente começa com maiúscula (convenção)
    def __init__(self, nome, ano_nasc):
        self.nome = nome
        self.ano_nasc = ano_nasc
    
    def calcular_idade(self):  # Adicionado 'self' e removido parâmetro extra
        idade = 2025 - self.ano_nasc  # Calcula a idade dentro do método
        if self.ano_nasc > 0 and self.ano_nasc <= 2025:  # Validação simples
            return f"Olá {self.nome}, com base em seu ano de nascimento, sua idade é {idade} anos"
        else:
            return "Você digitou seu ano de nascimento de maneira correta?"

# Capturando os dados do usuário
pnome = input("Olá, me diga seu nome: ")
panonasc = int(input("Agora me diga seu ano de nascimento: "))

# Criando o objeto
pessoa1 = Pessoa(pnome, panonasc)

# Chamando o método e imprimindo o resultado
print(pessoa1.calcular_idade())

input()  # Mantém o terminal aberto
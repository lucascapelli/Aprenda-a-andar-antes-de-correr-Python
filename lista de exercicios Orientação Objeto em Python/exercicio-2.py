'''
Exercício:

Crie uma classe Pessoa que:

    Receba no construtor (__init__) o nome e a idade da pessoa.

    Tenha um método chamado falar que retorne a frase:
    "Olá, meu nome é [nome] e eu tenho [idade] anos."

Depois, crie um objeto da classe Pessoa com nome e idade, e chame o método falar para imprimir a frase.

'''

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
usuario1 = Pessoa('lucas', 21)
print(usuario1.falar())
'''
🎯 Desafio:

✅ Crie uma classe chamada Cachorro.
✅ Ela deve ter:

    atributo nome

    atributo idade
    ✅ Deve ter um método apresentar() que imprima:
    "Oi! Eu sou [nome] e tenho [idade] anos caninos."


'''
class Catioro:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Oi! Eu sou {self.nome} e tenho {self.idade} anos caninos."
    
    def aniversario(self):
        self.idade = self.idade + 1
    
cachorro = Catioro('Mel',2)
print(cachorro.apresentar())
cachorro.aniversario()
print(cachorro.apresentar())
cachorro.aniversario()
print(cachorro.apresentar())
cachorro.aniversario()
print(cachorro.apresentar())


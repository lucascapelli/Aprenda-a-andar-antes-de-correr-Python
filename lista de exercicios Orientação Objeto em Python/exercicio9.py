class Funcionario:
    def __init__(self,nome,cargo,salário):
        self.nome = nome
        self.cargo = cargo
        self.salario = salário

    def exibir_dados(self):
        return f"dados do funcionário: Nome: {self.nome} cargo: {self.cargo} salário: {self.salario:.2f} R$"
    
    def aumentar_salario(self,porcentagem):
        self.salario += ((porcentagem * self.salario) / 100)
        return f"agora o salário do {self.nome} no cargo {self.cargo} é de {self.salario:.2f} R$"

    def trocar_cargo(self, cargo_novo):
        self.cargo = cargo_novo
        return f"agora o funcionário {self.nome} trabalha no cargo {self.cargo} "

f1 = Funcionario ('joão','auxiliar administrativo',1800)

print(f1.exibir_dados())
print(f1.trocar_cargo('Administrativo Pleno'))
print(f1.aumentar_salario(50))
print(f1.exibir_dados())

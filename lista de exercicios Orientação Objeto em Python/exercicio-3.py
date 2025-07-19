'''
Exercício OO nível intermediário:

Crie uma classe ContaBancaria que tenha:

    Atributos:

        titular (nome da pessoa)

        saldo (valor atual da conta, inicialize com 0)

    Métodos:

        depositar(valor) → adiciona o valor ao saldo

        sacar(valor) → subtrai o valor do saldo, se houver saldo suficiente; caso contrário, retorna uma mensagem de saldo insuficiente

        extrato() → retorna uma string com o nome do titular e o saldo atual formatado

'''
class ContaBancária:
    def __init__(self,titular,saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print(f'Saldo insuficiente\nSaldo Atual: {self.saldo}')

    def extrato(self):
        return f'Titular: {self.titular}\nSaldo em conta: {self.saldo}'
    






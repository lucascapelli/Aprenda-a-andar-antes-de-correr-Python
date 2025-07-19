class ContaBancaria:
    def __init__(self, titular, saldo=0):  # Saldo inicia como 0 por padrão
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        deposito = float(input("Digite o valor do depósito: "))
        self.saldo += deposito  # Agora realmente adiciona ao saldo
        return f"Olá {self.titular}, seu saldo final é de: R$ {self.saldo:.2f}"

    def sacar(self):
        saque = float(input("Digite o valor do saque: "))
        if saque > self.saldo:
            return "Valor insuficiente para esse saque."
        else:
            self.saldo -= saque  # Agora realmente desconta do saldo
            return f"Olá {self.titular}, seu saldo final é de: R$ {self.saldo:.2f}"

    def exibir_saldo(self):
        return f"{self.titular}, seu saldo atual é: R$ {self.saldo:.2f}"


# Criando uma conta
p1 = ContaBancaria("Julio", 1000)

# Testando os métodos
print(p1.exibir_saldo())  # Mostra saldo antes
print(p1.depositar())  # Faz um depósito
print(p1.sacar())  # Faz um saque
print(p1.exibir_saldo())  # Mostra saldo depois

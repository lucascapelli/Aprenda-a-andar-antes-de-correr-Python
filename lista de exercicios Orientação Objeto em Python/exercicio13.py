
class ContaBancaria:
    def _init_(self,titular,saldo):

        self.titular = titular
        self.saldo = saldo
    
    def depositar(self):
        valor = float(input("digite o valor do depósito: "))
        total = self.saldo + valor
        print(f"o seu saldo atual após o depósito é de{total}")

    def sacar(self):
        valorsaque = float(input("digite o valor de saque: "))
        totals = self.saldo - valorsaque
        
        if self.saldo >= valorsaque:
            print(f"o seu saldo atual após o saque é de{totals}")
        else:
             print("saldo insuficente para este valor de saque")

titular1 = input("diga o seu nome para realizarmos a operação bancária: ")
saldo1 = 1000
titular1 = ContaBancaria(titular1,saldo1)
operacao = input("agora diga qual operação você irá fazer, saque, ou depósito")

if operacao == "deposito":
    print( titular1.depositar())
elif operacao =="saque":
        print( titular1.sacar())
else:
     print("operação não reconhecida")
    
'''
Corrigido pelo grok

class ContaBancaria:
    def __init__(self, titular, saldo):  # Corrigido para __init__
        self.titular = titular
        self.saldo = saldo  # Saldo não precisa ser privado aqui, mas poderia ser __saldo
    
    def depositar(self):
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:  # Validação para valor positivo
                self.saldo += valor  # Atualiza o saldo
                return f"O seu saldo atual após o depósito é de R${self.saldo:.2f}"
            else:
                return "Valor inválido! O depósito deve ser positivo."
        except ValueError:
            return "Digite um valor numérico válido!"

    def sacar(self):
        try:
            valorsaque = float(input("Digite o valor de saque: "))
            if valorsaque > 0:  # Validação para valor positivo
                if self.saldo >= valorsaque:  # Verifica saldo suficiente
                    self.saldo -= valorsaque  # Atualiza o saldo
                    return f"O seu saldo atual após o saque é de R${self.saldo:.2f}"
                else:
                    return "Saldo insuficiente para este valor de saque!"
            else:
                return "Valor inválido! O saque deve ser positivo."
        except ValueError:
            return "Digite um valor numérico válido!"

# Capturando dados do usuário
titular1 = input("Diga o seu nome para realizarmos a operação bancária: ")
saldo1 = 1000
conta = ContaBancaria(titular1, saldo1)  # Renomeei 'titular1' pra 'conta' pra evitar confusão
operacao = input("Agora diga qual operação você irá fazer, 'saque' ou 'deposito': ")

# Executando a operação
if operacao == "deposito":
    print(conta.depositar())
elif operacao == "saque":  # Corrigido pra consistência
    print(conta.sacar())
else:
    print("Operação não reconhecida")'''
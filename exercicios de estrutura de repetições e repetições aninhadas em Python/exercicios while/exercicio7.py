# Solicita a senha ao usuário pela primeira vez
senha = input("Olá usuário, digite sua senha: ")

# Enquanto a senha for diferente da correta, continua no loop
while senha != 'python123':
    print("Senha incorreta")
    # Pede novamente a senha
    senha = input("Quer tentar novamente? ")

# Quando sair do loop (ou seja, digitou a senha certa), exibe a mensagem:
print("Acesso concedido")

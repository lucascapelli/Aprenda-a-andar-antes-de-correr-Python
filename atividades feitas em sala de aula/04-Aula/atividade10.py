nome = input("digite seu nome:\n")
while len(nome)<3:
    nome = input("digite seu nome novamente:\n")

idade = int(input("digite sua idade:\n"))
while idade < 0 or idade > 150:
    idade = int(input("digite novamente a sua idade:\n"))

salario = float(input("digite seu salário:\n"))
while salario < 0:
    salario = float(input("digite novamente o seu salário:\n"))

sexo = input("digite seu sexo(h/m):\n")
while sexo not in ['h','m']:
    sexo = input("elu delu aqui não!!!! digite novamente o seu sexo(h/m):\n")


estado_civil = input("a primeira letra do seu estado civil(s/c/v/d)\n")
while estado_civil not in ['s','c','v','d']:
    estado_civil = input("Opção inválida! Digite (s)olteiro, (c)asado, (v)iúvo ou (d)ivorciado:\n").strip().lower()

print("\n✅ Cadastro realizado com sucesso!")



# 02-atividade.py
"""
Exercício 2:
Faça um programa que solicite ao usuário:
• Nome
• Idade
• Profissão
E mostre na tela as informações digitadas no formato:
"Olá, [nome], sua idade é [idade] anos e sua profissão é [profissão]."

Objetivo: aprender a usar input() para receber dados do usuário
e print() para mostrar resultados na tela.
"""

# input() sempre retorna STRING (texto).
# Se você precisa de número, converta com int() ou float().
# Exemplos de uso:
#   idade = int(input("Idade: "))        # converte direto para inteiro
#   altura = float(input("Altura: "))    # converte direto para float
# Ou receba como string e converta depois:
#   texto = input("Valor: ")
#   numero = int(texto)

# --- coleta de dados ---
nome = input("Digite seu nome: ")                  # string
idade = int(input("Agora digite sua idade: "))     # convertido para int
profissao = input("E digite sua profissão: ")      # string

# --- exibição dos dados ---
# Forma simples (com várias partes separadas por vírgula)
print("Olá,", nome, "sua idade é", idade, "anos e sua profissão é", profissao)

# Forma mais legível com f-string (recomendada)
print(f"Olá, {nome}, sua idade é {idade} anos e sua profissão é {profissao}")

# --- exemplo extra: número decimal (float) ---
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
print(f"Sua altura é {altura} m")

# Opcional: mantém o console aberto em alguns ambientes
input("Pressione Enter para sair...")

# Dicas rápidas:
# - input() retorna texto por padrão; 
# Use int() para converter para números inteiros,
# Ou float() para números decimáis.
# Isso é só um resumo para iniciantes.
# Documentação oficial do input(): https://docs.python.org/3/library/functions.html#input
# Não existe dev bom que não leia documentação, jovem gafanhoto ;)


# 01-atividade.py
"""
Exercício 1:
Crie um programa que escreva a famosa frase "Olá Mundo" na tela.
Objetivo: Aprender a usar a função print() e observar saída no console.
"""

# print() → serve para mostrar algo na tela
# Você pode mostrar:
# - uma frase: print("Olá Mundo")
# - o valor de uma variável: print(minha_variavel)
# - frases e variáveis juntos: print("O valor é", minha_variavel)

# Exemplo simples: mostrar texto e variáveis na tela

mensagem = "Olá Mundo"
print(mensagem)  # mostra: Olá Mundo
# O print acima exibe o valor que está armazenado na variável `mensagem`,
# que é uma string (texto).

# Podemos usar print sem variável:
print("Olá mundo (não veio de nenhuma variável)")

# Ou combinar texto e variável:
nome = "Lucas"
print("Oi,", nome)  # mostra: Oi, Lucas

# Regras básicas (sintaxe):
# - strings (texto) vão entre aspas: "texto" ou 'texto'
# - variáveis não usam aspas: nome
# - se quiser mostrar vários valores juntos, separe por vírgula dentro do print:
print(mensagem, "texto extra", nome, "mais texto")

# Dica moderna (opcional): f-strings deixam o código mais legível
print(f"Olá {nome}, sua mensagem: {mensagem}")

# Print é geralmente usado para mostrar valores e acompanhar o que o programa está fazendo em determinado ponto (debug rápido);
# isso é só um resumo para iniciantes. 
# O resto das funcionalidades está na documentação oficial: https://docs.python.org/3/library/functions.html#print
# Não existe dev bom que não leia documentação, jovem gafanhoto ;)

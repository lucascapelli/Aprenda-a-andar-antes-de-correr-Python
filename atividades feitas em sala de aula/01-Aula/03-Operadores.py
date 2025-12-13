# 03-atividade.py
"""
Exercício 3:
Escreva um programa que leia o valor gasto por um cliente em um restaurante.
O programa deve calcular:
• O valor do serviço (10% do total)
• O valor total a ser pago (conta + serviço)
E mostrar na tela:
• Valor da conta
• Valor do serviço
• Valor total
Objetivo: Aprender a fazer cálculos simples com valores inseridos pelo usuário.
"""

# No Python temos operadores matemáticos básicos:
#   + → soma
#   - → subtração
#   * → multiplicação
#   / → divisão
# Esses operadores nos permitem fazer cálculos simples para:
#   - calcular porcentagens
#   - somar valores
#   - calcular totais
# Exemplo:
# Variavel1 = 10
# Variavel2 = 10
# Variavel3 = Variavel1 * Variavel2
# Neste exemplo, a variável 3 receberia o valor da multiplicação de Variavel1 por Variavel2
# e poderia ser utilizado qualquer operador desejado nesta situação

# Solicitar o valor da conta (recebe um número decimal)
conta = float(input("Digite o valor da conta: R$"))  # Variável conta recebe o valor digitado e converte para decimal usando float

# Calcular o valor do serviço (10% da conta)
servico = conta * 0.10  # Calcula 10% da conta; ponto indica decimal no Python

# Calcular o valor total (soma da conta + serviço)
total = servico + conta  # Variável total recebe a soma da conta mais serviço

# Mostrar as informações calculadas
print(f"O valor da sua conta foi R${conta:.2f}, o valor do serviço foi R${servico:.2f} e o total a ser pago é R${total:.2f}")
#  .2f formata o número para exibir duas casas decimais, deixando a saída mais amigável
# Exemplo: ao invés de um número sair como 12,332423434, usando .2f ele sairia como 12,33

# input() para manter o console aberto (opcional)
input("Pressione Enter para sair...")

# Dicas rápidas:
# - Operadores numéricos trabalham com int e float, então preste atenção ao tipo de número que você está usando
# - A formatação :.2f não muda o valor da variável, ela apenas altera o que é exibido na saída
# - Para detalhes completos, veja a documentação oficial: https://docs.python.org/3/library/operator.html#arithmetic-operations
# Não existe dev bom que não leia documentação, jovem gafanhoto ;)

"""
Exercício 4: Calculadora de Equação do 2º Grau (Fórmula de Bhaskara)

Faça um programa que calcule as duas raízes de uma equação do 2º grau:
ax² + bx + c = 0

O programa deve solicitar os valores dos coeficientes a, b e c e assumir que as raízes são reais.

A fórmula para calcular as raízes de uma equação do 2º grau é a fórmula de Bhaskara:

      (consultar a formula no PDF)

Onde:
• Δ = b² - 4ac é o discriminante, que determina o tipo das raízes
• Se Δ > 0: existem duas raízes reais distintas
• Se Δ = 0: existe uma única raiz real (raiz dupla)
• Se Δ < 0: as raízes são complexas (não são reais)

Assim, para calcular as raízes:
•Raiz 1 (x₁):
    (consultar a formula no PDF)
•Raiz 2 (x₂):
    (consultar a formula no PDF)

Objetivo: Aprender estruturas condicionais e uso da biblioteca math
"""

import math  # No Python (e em várias outras linguagens) podemos 
# importar bibliotecas pra usar funções prontas, como sqrt.

# Vamos resolver uma equação do 2º grau ax² + bx + c = 0 usando a famosa fórmula de Bhaskara.
# Primeiro precisamos descobrir o valor de delta:
# Δ = b² - 4ac

# Passo 1: pegar os valores de a, b e c do usuário
a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))

# Passo 2: calcular delta
delta = b**2 - 4*a*c  # No Python usamos ** pra potência, então b**2 é b ao quadrado
print("O valor do delta é:", delta)

# Passo 3: verificar condições
if a == 0:  # SE a for zero, não dá pra calcular, porque não é mais uma equação do 2º grau
    print("O coeficiente 'a' não pode ser 0, jovem gafanhoto!")
elif delta >= 0:  # SE delta for positivo ou zero, temos raízes reais
    raiz_positiva = (-b + math.sqrt(delta)) / (2*a)  # Fórmula de Bhaskara: (-b + √Δ) / 2a
    raiz_negativa = (-b - math.sqrt(delta)) / (2*a)  # Fórmula de Bhaskara: (-b - √Δ) / 2a
    print("A raiz positiva é:", raiz_positiva)
    print("A raiz negativa é:", raiz_negativa)
else:  # SE delta for negativo, não existem raízes reais
    print("Delta negativo = sem raízes reais")

input("\nPressione Enter pra sair...")

# Dicas rápidas:
# - math.sqrt(x) calcula a raiz quadrada de x
# - if = SE, elif = SE não, faça, else = SENÃO
# - Para detalhes sobre math: https://docs.python.org/3/library/math.html
# - Para detalhes sobre condicionais: https://docs.python.org/3/tutorial/controlflow.html
# Lembre-se: ler a documentação é sempre bom, jovem gafanhoto ;)

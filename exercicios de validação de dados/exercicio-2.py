'''🧩 Missão 2: Sistema de notas

    Peça uma nota de 0 a 10. Depois, diga se o aluno:

    Tirou "Aprovado" (>= 7)

    Ficou em "Recuperação" (entre 5 e 6.9)

    Está "Reprovado" (< 5)'''

try:
    nota = float(input('Olá Professor\nDigite a nota do aluno (0 a 10):\n'))

    if nota < 0 or nota > 10:
        print('Nota inválida. Digite um valor entre 0 e 10.')
    elif nota >= 7:
        print('Aluno aprovado.')
    elif nota < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno de recuperação.')

except ValueError:
    print('Por favor, digite um número válido.')

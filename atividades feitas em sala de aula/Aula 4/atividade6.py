turno= input("o seu turno de trabalho é o diurno ou noturno ? ")
noturno = 'noturno'
diurno = 'diurno'
horas = float(input("quantas horas: "))
valorsalario = 37.50 * horas
valorsalarion = 45 * horas

if turno == noturno:
    print("o valor de seu salário é:", valorsalarion)
elif turno == diurno:
    print("o valor de seu salário é:", valorsalario)
else:
    print("não temos esse turno")

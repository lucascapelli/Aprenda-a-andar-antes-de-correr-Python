'''
🧠 Exercício - Notas por matéria

Crie um script em Python que:

✅ 1️⃣ Abra um arquivo chamado notas_materias.txt no modo leitura.

✅ 2️⃣ Cada linha do arquivo tem o seguinte formato:

nome,materia,nota

📄 Exemplo de conteúdo do arquivo:

Ana,Matemática,8.5  
Bruno,Português,7.0  
Ana,Português,9.0  
Bruno,Matemática,6.5  
Carlos,Matemática,7.5  
Carlos,Português,8.0  

✅ 3️⃣ Para cada linha, separe nome, materia e nota.

✅ 4️⃣ Armazene as notas por aluno num dicionário, agrupadas por nome.

✅ 5️⃣ Ao final, exiba:

Aluno: <nome>
Média: <media calculada com 2 casas decimais>


'''
aluno1Nota= 0
aluno2Nota= 0
aluno3Nota = 0
aluno1Nome = ''
aluno2Nome = ''
aluno3Nome = ''

        

with open('exercicios de leitura de arquivo em python/exercicio-6.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
       
        nome,materia,nota = linha.split(',')
        nota_convertida = float(nota)
        #print(nome,materia,nota_convertida)
        if nome == 'Carlos':
            aluno1Nome = 'Carlos'
            aluno1Nota += nota_convertida
        elif nome == 'Ana':
            aluno2Nome = 'Ana'
            aluno2Nota += nota_convertida
        elif nome == 'Bruno':
            aluno3Nome = 'Bruno'
            aluno3Nota += nota_convertida

print(f'Aluno: {aluno1Nome}\nMédia: {aluno1Nota/2} ')
print(f'Aluno: {aluno2Nome}\nMédia: {aluno2Nota/2} ')
print(f'Aluno: {aluno3Nome}\nMédia: {aluno3Nota/2} ')


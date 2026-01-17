'''
Exercício – CRUD com foco em lógica (Python + MySQL)

Este arquivo demonstra a sequência típica de operações CRUD usando
mysql.connector (driver oficial MySQL para Python).

Conceitos e sintaxe importantes (resumo prático):

1) Conexão e cursor
   - conn = mysql.connector.connect(...) abre uma conexão TCP com o servidor MySQL.
   - cursor = conn.cursor() cria um objeto cursor que envia comandos SQL ao servidor.
   - Existem cursors que retornam dicionários (cursor = conn.cursor(dictionary=True)),
     mas o padrão retorna tuplas.

2) Execução de queries
   - cursor.execute(query, params=None)
     - Quando 'params' é informado (tupla/lista), o driver aplica escape/parametrização
       apropriada e previne SQL injection. Exemplo:
         query = "INSERT INTO autores (nome, pais) VALUES (%s, %s)"
         cursor.execute(query, (nome, pais))
   - Para executar a mesma query várias vezes com diferentes parâmetros, use
     cursor.executemany(query, seq_of_params).

3) Commit e transações
   - Por padrão, alterações (INSERT/UPDATE/DELETE/DDL) ficam em uma transação local.
   - Use conn.commit() para persistir (confirmar) a transação no servidor.
   - Em caso de erro, chame conn.rollback() para reverter mudanças pendentes.

4) Leitura de resultados
   - cursor.fetchall() retorna todas as linhas do resultado como lista de tuplas:
     [(col1, col2, ...), (col1, col2, ...), ...]
   - cursor.fetchone() retorna a próxima linha ou None.
   - A ordem das colunas na tupla segue a ordem do SELECT.

5) Metadados úteis
   - cursor.lastrowid contém o id gerado pelo último INSERT (quando suportado).

6) Boas práticas (padrão try/except/finally)
   try:
       conn = mysql.connector.connect(...)
       cursor = conn.cursor()
       cursor.execute(...)
       conn.commit()
   except mysql.connector.Error as e:
       conn.rollback()
       print('Erro:', e)
   finally:
       cursor.close()
       conn.close()

7) Segurança e performance
   - Sempre parametrizar queries que recebem dados do usuário.
   - Use índices no banco para acelerar WHERE/JOINS.
   - Use executemany() para inserir muitos registros de forma eficiente.

O script abaixo mantém a lógica do exercício: criar tabela, inserir autores,
mostrar, atualizar e apagar, com commits após operações que modificam o banco.
'''

import mysql.connector

# Conexão com o banco
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root@123',
    database='Biblioteca'
)

# cursor para executar comandos SQL
cursor = conn.cursor()

# Criar tabela com regra de unicidade para evitar duplicação
cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) UNIQUE,
        pais VARCHAR(50)
    )
''')

# Inserir autores (INSERT IGNORE evita erro caso o nome já exista)
cursor.execute('''
    INSERT IGNORE INTO autores (nome, pais)
    VALUES
        ('Ayn Rand', 'Russia'),
        ('J.K Rowling', 'Inglaterra'),
        ('George Orwell', 'Inglaterra')
''')
# confirma inserções
conn.commit()

# Ler todos os autores — SELECT traz os registros e fetchall os retorna como lista de tuplas
cursor.execute('SELECT * FROM autores')
autores = cursor.fetchall()
print("Autores cadastrados:", autores)

# Atualizar país de um autor específico — demonstra UPDATE e commit
cursor.execute('''
    UPDATE autores
    SET pais = 'Brasil'
    WHERE nome = 'Ayn Rand'
''')
conn.commit()

# Atualizar nome de um autor específico — outro exemplo de UPDATE
cursor.execute('''
    UPDATE autores
    SET nome = 'Ayn R.'
    WHERE nome = 'Ayn Rand'
''')
conn.commit()

# Deletar um autor específico — DELETE e commit
cursor.execute('''
    DELETE FROM autores
    WHERE nome = 'Ayn R.'
''')
conn.commit()

# Confirmar a exclusão com um novo SELECT
cursor.execute('SELECT * FROM autores')
autores = cursor.fetchall()
print("Autores após exclusão:", autores)

# Fechar cursor e conexão para liberar recursos
cursor.close()
conn.close()

# Dicas extras:
# - usar INSERT parametrizado quando inserir dados vindos do usuário
# - tratar exceções com try/except e usar conn.rollback() em caso de erro
# - confirmar (commit) após operações que modificam o banco

'''
Exercício

Crie um banco de dados chamado Biblioteca (ou use um existente).

Crie uma tabela livros com as seguintes colunas:

id (inteiro, chave primária, auto-incremento)
titulo (texto)
autor (texto)
ano (inteiro)
preco (float)

Objetivo: praticar CRUD usando Python e MySQL.

Observações importantes sobre a interação Python <-> MySQL (mysql.connector):
- conn = mysql.connector.connect(...) abre uma conexão com o servidor MySQL.
- cursor = conn.cursor() cria um cursor que envia comandos SQL ao servidor.
- cursor.execute(query, params) executa uma query; passando 'params' o driver faz a "parametrização" (previne SQL injection).
- cursor.executemany(query, seq_of_params) executa a mesma query várias vezes com diferentes parâmetros.
- Para persistir alterações (INSERT/UPDATE/DELETE/DDL) é necessário chamar conn.commit(); sem commit a transação pode não ser gravada.
- Em caso de erro, use conn.rollback() para desfazer a transação pendente.
- cursor.fetchall() retorna todas as linhas do resultado como lista de tuplas: [(id, titulo, autor, ano, preco), ...]
- cursor.lastrowid contém o id gerado pelo último INSERT (quando aplicável e suportado pelo driver), útil para chaves auto-increment.
- Sempre feche cursor e conexão (cursor.close(); conn.close()) ou use try/finally.
'''

import mysql.connector

# conexão com o banco
# host: endereço do servidor; user/password: credenciais; database: schema a ser usado
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root@123',
    database='Biblioteca'
)

# o cursor é o ponto de contato para enviar SQL ao servidor
cursor = conn.cursor()

# CREATE TABLE: definição de esquema SQL (DDL)
# VARCHAR(100) define uma coluna de texto com tamanho máximo; FLOAT para valores decimais
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(100),
        autor VARCHAR(100),
        ano INT,
        preco FLOAT
    )
''')

# INSERT (Create) — aqui usamos uma única instrução com múltiplos VALUES.
# Alternativa segura (quando dados vêm de usuário) — usar parametrização:
# query = "INSERT INTO livros (titulo, autor, ano, preco) VALUES (%s, %s, %s, %s)"
# params = ('1984', 'George Orwell', 1949, 39.90)
# cursor.execute(query, params)

cursor.execute('''
    INSERT INTO livros (titulo, autor, ano, preco)
    VALUES
        ('Senhor dos Anéis', 'J.R.R Tolkien', 1954, 64.99),
        ('A revolução dos Bichos', 'George Orwell', 1945, 29.90),
        ('1984', 'George Orwell', 1949, 39.90)
''')

# confirma as alterações: commit aplica a transação no banco
conn.commit()

# SELECT (Read) — executar query de leitura e buscar o resultado
cursor.execute('SELECT * FROM livros')
livros = cursor.fetchall()
# fetchall() retorna lista de tuplas; cada tupla corresponde a uma linha (colunas na ordem do SELECT)
print('Após INSERT:')
print(livros)

# UPDATE — modifica registros
cursor.execute('''
    UPDATE livros
    SET ano = 1950
    WHERE titulo = '1984'
''')
# confirmar a alteração
conn.commit()

cursor.execute('SELECT * FROM livros')
print('Após UPDATE:')
print(cursor.fetchall())

# DELETE — remove registros que atendem à condição
cursor.execute('''
    DELETE FROM livros
    WHERE titulo = '1984'
''')
# confirmar remoção
conn.commit()

cursor.execute('SELECT * FROM livros')
print('Após DELETE:')
print(cursor.fetchall())

# fechar cursor e conexão quando não são mais necessários — libera recursos
cursor.close()
conn.close()

# Boas práticas resumidas:
# - sempre parametrizar queries que recebem dados externos: cursor.execute(query, params)
# - usar try/except para capturar erros e conn.rollback() quando necessário
# - preferir cursor.executemany() ao inserir muitos registros de uma só vez
# - fechar conexões no finally/with para garantir liberação de recursos

# P.S: por conta do objetivo desse repo ser python
# não dá para explicar tudo de SQL aqui igual fazemos com python


# Antes de poder nos comunicar com o banco de dados precisamos
# primeiro criar o nosso ambiente virtual com a nossa pasta venv
# então no terminal rodamos o comando:
# python -m venv venv

'''a pasta venv é importante porque ela isola as dependências do projeto
    das dependências do sistema operacional, evitando conflitos entre versões
    de pacotes e garantindo que o projeto funcione corretamente em diferentes
    ambientes.'''

# logo criarmos ela, precisamos ativá-la no nosso terminal
# para que ele passe a ser o ambiente padrão do nosso projeto
# ou seja não basta ter a pasta venv, precisamos ativá-la também
# no terminal rodamos o comando:
'''
no windows:
    venv/Scripts/activate
no linux ou mac:
    source venv/bin/activate
'''


# e ainda mais um passo depois disso é escolher o path correto no
# nosso editor de código, no caso o vscode, para que ele também
# utilize o ambiente virtual do nosso projeto
'''Abra o projeto no VS Code.

Ctrl+Shift+P → “Python: Select Interpreter”

Procure pelo caminho do seu venv:

~/Documentos/Exercicios em Python/venv/bin/python

Selecione o caminho do venv e agora sim o VS Code estará utilizando
o ambiente virtual do seu projeto.'''

import mysql.connector #dai basta nós importar a biblioteca mysql.connector

# agora precisamos criar a conexão com o banco de dados
# e nós temos vários tipo de conexões, com um banco de dados
# sendo elas:
# conn
# cursor
# execute
# fetchall

# aqui por exemplo nós vamos criar a conexão com o banco de dados
# através do conn
# e de maneira simples nós fazemos nós:

# criamos uma variável chamada conn que recebe a função
# mysql.connector.connect() que é a função que cria a conexão
# com o banco de dados, e dentro dessa função nós passamos os
# parâmetros necessários para a conexão, como:
conn = mysql.connector.connect(
    host='localhost', # o host é o endereço do servidor do banco de dados
    # aqui estamos utilizando o localhost que é o endereço do
    # próprio computador, mas poderia ser um endereço de um servidor
    # remoto também, como por exemplo um servidor na nuvem
    
    user='root', # o user é o usuário do banco de dados
    
    password='Root@123', # a password é a senha do usuário do banco de dados

    database='EstudoCrud' # o database é o nome do banco de dados
)

# Depois de criar a conexão (conn) precisamos de um cursor.
# O cursor é o objeto que enviará comandos SQL ao servidor e
# permitirá recuperar resultados (com fetchall, fetchone etc.).
# Em muitos drivers o cursor também mantém estado sobre a última
# execução (por exemplo, cursor.lastrowid após INSERT).
cursor = conn.cursor() # criamos uma variável chamada cursor que recebe a função
# conn.cursor() que é a função que cria o cursor através da conexão
# que nós criamos anteriormente.

# agora nós podemos executar comandos SQL através do cursor
# por exemplo, para criar uma tabela chamada clientes, nós fazemos o seguinte:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes ( 
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100)
    )
    ''')
# O python rodando o código acima vai criar uma tabela chamada clientes
# caso ela não exista, com três colunas: id, nome e email.

# IMPORTANTE: operações que alteram o banco (CREATE, INSERT, UPDATE, DELETE)
# ficam numa transação até que você confirme com conn.commit().
# Sem o commit, as alterações podem não ser visíveis para outras sessões
# ou podem ser descartadas ao fechar a conexão.

# Exemplo de INSERT: aqui inserimos um registro na tabela clientes.
cursor.execute('''
    INSERT INTO clientes (nome, email)
    VALUES ('João Silva', 'joao.silva@example.com')
''')
# Após executar o INSERT é necessário confirmar a transação:
conn.commit()  # <-- confirma as alterações no banco (persistência)

# Para ler dados usamos SELECT e fetchall() para trazer todas as linhas
cursor.execute('''SELECT * FROM clientes''')
clientes = cursor.fetchall(
)

# cursor.fetchall() retorna uma lista de tuplas (cada tupla = uma linha)
print(clientes)

# Boas práticas (não obrigatórias aqui, mas recomendadas):
# - usar consultas parametrizadas em vez de string formatada para evitar SQL injection
# - fechar cursor e conexão ao finalizar: cursor.close(); conn.close()
# - usar try/except/finally para garantir rollback em caso de erro
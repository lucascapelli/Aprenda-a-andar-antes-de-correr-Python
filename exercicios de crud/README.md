# Exercícios de CRUD — Python + MySQL

Conjunto de scripts para praticar operações básicas de CRUD (Create, Read, Update, Delete) usando o driver mysql.connector em Python.

Arquivos principais

- `crud-01.py` — Exemplo mínimo: cria a tabela `clientes`, insere um registro e lista os clientes. Mostra como usar `cursor.execute()`, `conn.commit()` e `cursor.fetchall()`.
- `crud-02.py` — Tabela `livros`: demonstra INSERT, SELECT, UPDATE e DELETE com commits entre operações. Inclui comentários sobre parametrização e formato de retorno de `fetchall()`.
- `crud-o3.py` — Tabela `autores`: fluxo completo (criar tabela, inserir autores, listar, atualizar e excluir). Contém explicações técnicas sobre transações, `cursor.lastrowid`, parametrização e padrão try/except/finally.

Pré-requisitos

- Python 3.8+
- MySQL/MariaDB em execução local ou remota
- Pacote: `mysql-connector-python` (instale com `pip install mysql-connector-python`)

Como executar

1. Ajuste credenciais de conexão nos arquivos (`host`, `user`, `password`, `database`).
2. Execute: `python crud-01.py` ou `python crud-02.py` ou `python crud-o3.py`.

Notas e boas práticas

- Sempre use `conn.commit()` após operações que modificam o banco; sem commit as mudanças podem não ser persistidas.
- Prefira consultas parametrizadas para inserir dados dinâmicos: `cursor.execute(query, params)` para evitar SQL injection.
- Trate exceções e use `conn.rollback()` em caso de erro; feche cursor/conn no `finally`.
- Em scripts de produção, evite deixar credenciais em código-fonte (use variáveis de ambiente ou arquivos de configuração).

Observação

Este repositório é mantido no meu tempo livre e está em construção — melhorias e correções serão adicionadas gradualmente.
"""
Arquivo __init__.py do app core.

Este arquivo indica ao Python que este diretório deve ser tratado
como um pacote Python.

👉 Mesmo vazio, ele é importante para:
- permitir imports entre arquivos do app
- organizar o código em módulos
- garantir que o Django reconheça corretamente o app

Em Python, arquivos __init__.py existem para:
- inicializar pacotes
- controlar o que é exposto ao importar um módulo
- organizar projetos grandes de forma clara e modular

Na prática, muitos __init__.py ficam vazios,
mas sua presença é essencial para a estrutura do projeto,
especialmente em projetos extensos.

📁 Exemplo de organização usando __init__.py:

core/
├── models/
│   ├── __init__.py
│   ├── pessoa.py
│   └── endereco.py
├── views/
│   ├── __init__.py
│   ├── pessoa_views.py
│   └── auth_views.py
├── urls.py
└── apps.py

📄 Exemplo de __init__.py (models/__init__.py):

from .pessoa import Pessoa
from .endereco import Endereco

Assim, ao importar:
from core.models import Pessoa

o Python sabe exatamente de onde esse model vem,
mesmo ele estando em arquivos separados.

📚 Documentação oficial:
https://docs.python.org/3/tutorial/modules.html#packages
"""

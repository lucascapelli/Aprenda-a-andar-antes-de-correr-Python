"""
Arquivo de configuração WSGI do projeto Django.

Este arquivo é o ponto de entrada da aplicação quando ela é executada
em um servidor web (ex: Gunicorn, uWSGI, Apache, Nginx).

👉 Ele não é usado diretamente no desenvolvimento com runserver,
mas é essencial em ambientes de produção, por isso também é importante
entender seu funcionamento.


Documentação oficial:
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Define qual arquivo de settings o Django deve usar
# Isso permite que o servidor saiba como configurar o projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrudBasico.settings')

# Cria a aplicação WSGI que será chamada pelo servidor web
# O servidor usa esse objeto para encaminhar requisições HTTP ao Django
application = get_wsgi_application()

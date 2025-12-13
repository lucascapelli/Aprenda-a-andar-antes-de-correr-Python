"""
Arquivo de configuração do app core.

Este arquivo define informações básicas do aplicativo
e permite que o Django reconheça e inicialize o app corretamente.

👉 Cada app Django pode (e deve) ter seu próprio AppConfig.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    # Nome do app dentro do projeto
    # Deve corresponder ao diretório do app
    name = 'core'

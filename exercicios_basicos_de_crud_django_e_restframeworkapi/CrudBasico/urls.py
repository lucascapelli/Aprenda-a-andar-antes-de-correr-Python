"""
Arquivo principal de configuração de URLs do projeto.

Aqui são definidos os caminhos principais da aplicação.
Esse arquivo funciona como a "porta de entrada" das URLs,
direcionando cada caminho para o app ou sistema responsável.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL do painel administrativo padrão do Django
    # Permite gerenciar os dados do banco (CRUD) via interface pronta
    path('admin/', admin.site.urls),

    # Inclui as URLs definidas no app core
    # Todas as rotas do core começam a ser resolvidas a partir da raiz '/'
    path('', include('core.urls')),
]

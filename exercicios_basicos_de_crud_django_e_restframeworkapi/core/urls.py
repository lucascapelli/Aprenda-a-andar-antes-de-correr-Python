# As URLs do app core definem quais caminhos o navegador pode acessar
# e qual view será executada para cada caminho.
from django.urls import path
from . import views  # Importa as views do app

urlpatterns = [
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    # 'pessoas/' → caminho acessado no navegador
    # views.lista_pessoas → view e function executadas
    # name → nome da rota usado para gerar a URL 'pessoas/' no navegador
]

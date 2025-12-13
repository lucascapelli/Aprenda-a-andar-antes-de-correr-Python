from django.contrib import admin
from core.models import Pessoa

# O Django Admin é um painel pronto que permite ao desenvolvedor
# visualizar, criar, editar e excluir dados do banco de forma rápida,
# sem precisar criar telas no frontend.
#
# Tudo o que é registrado aqui aparece em:
# http://127.0.0.1:8001/admin/
# Observação: essa URL é definida no arquivo de URLs principal do projeto
# e não nas URLs do app core.

# Registra o model Pessoa no painel administrativo
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):

    # Define quais informações de cada Pessoa aparecem na tela de listagem
    # do admin (antes de abrir o detalhe do registro)
    list_display = ('nome', 'idade', 'genero')

    # Cria filtros na lateral do admin para facilitar a busca
    # por registros específicos (ex: filtrar por gênero)
    list_filter = ('genero',)

    # Ativa um campo de pesquisa no topo do admin,
    # permitindo buscar Pessoas pelo nome
    search_fields = ('nome',)

from django.shortcuts import render
from .models import Pessoa

# Diferente de um método de classe, que recebe `self` como referência da instância,
# uma view baseada em função recebe o objeto `request`.
#
# O `request` representa a requisição HTTP (Hypertext Transfer Protocol)
# e contém todas as informações da chamada, como método, usuário,
# dados enviados e cabeçalhos.
#
# É através desse objeto que a view consegue processar a requisição
# mapeada pela URL definida em core/urls.py.

def lista_pessoas(request):
   # 1) Busca todas as pessoas salvas no banco de dados
    # através do model Pessoa
    pessoas = Pessoa.objects.all()

    # 2) Cria um dicionário com os dados que serão enviados ao template
    contexto = {
        'pessoas': pessoas
    }

    # 3) Renderiza o template HTML com os dados do contexto
    return render(request, 'core/lista_pessoas.html', contexto)

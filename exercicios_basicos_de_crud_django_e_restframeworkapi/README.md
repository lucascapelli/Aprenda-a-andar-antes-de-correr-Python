# 📘 README --- Django CRUD Básico + DRF

Guia Educacional para Iniciantes

Um guia passo a passo para criar seu primeiro backend Django com Django
REST Framework, explicando o propósito e a importância de cada etapa
para novos programadores.

------------------------------------------------------------------------

## 🔧 1. Criar o Ambiente de Trabalho

### ▶️ 1.1 Criar a pasta do projeto

``` bash
mkdir nome_do_projeto
cd nome_do_projeto
```

**Explicação:** Cria uma pasta dedicada para seu projeto, organizando
tudo em um único local.

### ▶️ 1.2 Criar um ambiente virtual

``` bash
python3 -m venv .venv
```

**Por que usar ambiente virtual?**\
Isola as dependências deste projeto das outras instalações Python da sua
máquina.

### ▶️ 1.3 Ativar o ambiente virtual

**Linux/macOS:**

``` bash
source .venv/bin/activate
```

**Windows:**

``` bash
.venv\Scripts\activate
```

------------------------------------------------------------------------

## 📦 2. Instalar Dependências

``` bash
pip install django djangorestframework
```

### O que são dependências?

-   **Django:** Framework web principal\
-   **DRF:** Extensão para criar APIs RESTful

------------------------------------------------------------------------

## 🧱 3. Criar o Projeto Django

``` bash
django-admin startproject CrudBasico .
```

O ponto final (`.`) faz o projeto ser criado na pasta atual.

Estrutura criada: - `manage.py` - `CrudBasico/`

------------------------------------------------------------------------

## 🚧 4. Criar o App

``` bash
python manage.py startapp core
```

**Projeto ≠ App:**\
Projeto = site inteiro\
App = funcionalidade específica

------------------------------------------------------------------------

## 🛠 5. Registrar o App em `settings.py`

``` python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'core',
]
```

Isso permite que Django reconheça seu app e o DRF.

------------------------------------------------------------------------

## 🗄 6. Criar os Modelos --- `core/models.py`

``` python
from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
```

Modelos representam tabelas no banco de dados.

------------------------------------------------------------------------

## 💽 7. Migrações

``` bash
python manage.py makemigrations
python manage.py migrate
```

-   `makemigrations`: cria blueprint\
-   `migrate`: aplica no banco

------------------------------------------------------------------------

## 🔌 8. Criar o Serializer --- `core/serializers.py`

``` python
from rest_framework.serializers import ModelSerializer
from .models import Tarefa

class TarefaSerializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
```

Serializers convertem modelos ↔ JSON.

------------------------------------------------------------------------

## 🌐 9. Criar as Views --- `core/views.py`

``` python
from rest_framework.viewsets import ModelViewSet
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
```

`ModelViewSet` já fornece CRUD completo.

------------------------------------------------------------------------

## 🛣 10. Rotas da API --- `CrudBasico/urls.py`

``` python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import TarefaViewSet

router = DefaultRouter()
router.register('tarefas', TarefaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
```

O router cria rotas automaticamente.

------------------------------------------------------------------------

## ▶️ 11. Rodar o Servidor

``` bash
python manage.py runserver 8001
```

Teste em:\
http://localhost:8001/tarefas/

------------------------------------------------------------------------

## 🧪 12. Testar sua API

### ▶️ 12.1 No Navegador

-   Listar: `/tarefas/`
-   Detalhes: `/tarefas/1/`

Interface do DRF facilita os testes.

### ▶️ 12.2 Usando cURL

**GET**

``` bash
curl http://localhost:8001/tarefas/
```

**POST**

``` bash
curl -X POST http://localhost:8001/tarefas/ -H "Content-Type: application/json" -d '{"titulo":"Estudar Django","descricao":"Aprender DRF","concluido":false}'
```

**PUT**

``` bash
curl -X PUT http://localhost:8001/tarefas/1/ -H "Content-Type: application/json" -d '{"titulo":"Atualizado","descricao":"Editado via curl","concluido":true}'
```

**DELETE**

``` bash
curl -X DELETE http://localhost:8001/tarefas/1/
```

------------------------------------------------------------------------

## 📚 Conceitos-Chave Aprendidos

-   **MVT (Model-View-Template)**
-   **ORM**
-   **Serialização**
-   **API RESTful**
-   **CRUD Completo**

------------------------------------------------------------------------

Feito para estudo e prática ❤️

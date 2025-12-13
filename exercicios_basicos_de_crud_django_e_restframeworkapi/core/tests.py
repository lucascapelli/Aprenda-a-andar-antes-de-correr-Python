"""
Arquivo de testes do Django (tests.py).

Este arquivo contém os testes automatizados da aplicação.
Os testes são importantes para garantir que o código funcione corretamente
e que mudanças futuras não quebrem funcionalidades existentes.

👉 O Django fornece o framework de testes através da classe TestCase,
que permite testar modelos, views, formulários, etc.

📁 Exemplo básico de testes com TestCase:

from django.test import TestCase
from core.models import Pessoa

class PessoaTestCase(TestCase):
    def setUp(self):
        Prepara o ambiente para o teste
        self.pessoa = Pessoa.objects.create(nome="Lucas", idade=30)

    def test_pessoa_nome(self):
        Testa se o nome da pessoa está correto
        self.assertEqual(self.pessoa.nome, 'Lucas')

    def test_pessoa_idade(self):
        Testa se a idade da pessoa está correta
        self.assertEqual(self.pessoa.idade, 30)

📚 Documentação oficial sobre testes no Django:
https://docs.djangoproject.com/en/6.0/topics/testing/
"""

# Importa a classe TestCase do Django para criar testes
from django.test import TestCase


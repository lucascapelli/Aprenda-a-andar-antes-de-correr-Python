"""
=== DJANGO MODELS - GUIA RÁPIDO ===

COMO FUNCIONA?
---------------
1. HERANÇA: class NomeModel(models.Model)
   - models.Model dá superpoderes de banco de dados à sua classe
   - Automaticamente vira tabela no banco
   - Ganha métodos: save(), delete(), objects.all(), filter(), etc.

2. FIELDS (CAMPOS) = COLUNAS DO BANCO
   - Cada field representa uma coluna na tabela
   - Define o tipo de dado que será armazenado
   - Exemplos:
     • CharField(max_length=100) → VARCHAR(100)
     • DecimalField(max_digits=10, decimal_places=2) → DECIMAL(10,2)
     • IntegerField() → INT
     • BooleanField() → BOOLEAN
     • DateField() → DATE

3. verbose_name = "NOME BONITO PARA HUMANOS"
   - Aparece no Admin Django, formulários, mensagens de erro
   - Sem ele: "data_nasc" → Com ele: "Data de Nascimento"
   - Melhora a experiência do usuário/admin

4. help_text = "INSTRUÇÃO/AJUDA NO FORMULÁRIO"
   - Texto explicativo abaixo do campo
   - Pode ser: formato esperado, regras, exemplos
   - Ex: help_text="Digite no formato DD/MM/AAAA"

EXEMPLO PRÁTICO:
----------------
class Produto(models.Model):  # 1. Herda de models.Model
    nome = models.CharField(   # 2. Field tipo texto
        max_length=100,
        verbose_name="Nome do Produto",   # 3. Nome amigável
        help_text="Digite o nome completo do produto"  # 4. Instrução
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço",
        help_text="Valor em reais (R$)"
    )

    def __str__(self):
        return self.nome  # Representação em string

    class Meta:
        ordering = ['nome']  # Ordenação padrão

PARA USAR:
----------
1. python manage.py makemigrations  # Cria migrações
2. python manage.py migrate         # Aplica ao banco
3. No código: Produto.objects.create(nome="...", preco=...)

LEMBRE-SE:
----------
- DecimalField para dinheiro (NÃO FloatField!)
- CharField sempre precisa de max_length
- null=True (banco) ≠ blank=True (formulário)
- unique=True evita duplicados
- auto_now_add=True (criação) vs auto_now=True (atualização)

DOCUMENTAÇÃO: https://docs.djangoproject.com/en/stable/topics/db/models/
"""

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(
        max_length= 50,
        verbose_name='Nome',
        help_text='Digite seu nome completo.'
    )

    idade = models.IntegerField(
        verbose_name='idade',
        help_text='Digite sua idade:'
    )
    
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    genero = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES,
        default='M',  # opcional
        verbose_name="Gênero"
    )
    def __str__(self):
        return self.nome, self.idade, self.genero
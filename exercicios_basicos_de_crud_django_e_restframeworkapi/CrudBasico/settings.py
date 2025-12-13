"""
Arquivo de configurações principais do projeto Django.

Este arquivo controla o comportamento global da aplicação:
banco de dados, apps instalados, templates, idioma, fuso horário,
segurança e arquivos estáticos.

👉 Em projetos reais, este arquivo é essencial para entender
como o Django funciona por dentro.
"""

from pathlib import Path

# ============================================================
# BASE DO PROJETO
# ============================================================
# Define o diretório raiz do projeto
# Usado como referência para caminhos de arquivos (db, templates, etc)
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# CONFIGURAÇÕES INICIAIS (DESENVOLVIMENTO)
# ============================================================
# ⚠️ Quick-start development settings - unsuitable for production
# Documentação:
# https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# Chave secreta usada pelo Django para segurança interna
# ⚠️ Nunca deve ser exposta em produção
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#secret-key
SECRET_KEY = 'django-insecure-!1ydm$ka914xkgr7uja1omo-3tk#=sbo@29cp@0%hvzahxh_pd'

# Ativa mensagens de erro detalhadas
# ⚠️ Deve ser False em produção
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#debug
DEBUG = True

# Define quais hosts podem acessar a aplicação
# Em desenvolvimento pode ficar vazio
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


# ============================================================
# APLICAÇÕES INSTALADAS
# ============================================================
# Lista de apps que o Django carrega no projeto
# Inclui apps internos do Django e apps criados por você
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#installed-apps
INSTALLED_APPS = [
    'django.contrib.admin',        # Painel administrativo
    'django.contrib.auth',         # Sistema de autenticação
    'django.contrib.contenttypes', # Tipos de conteúdo do Django
    'django.contrib.sessions',     # Gerenciamento de sessões
    'django.contrib.messages',     # Sistema de mensagens
    'django.contrib.staticfiles',  # Arquivos estáticos (CSS, JS, imagens)

    'core',                        # App principal do projeto
]


# ============================================================
# MIDDLEWARE
# ============================================================
# Camadas que processam a requisição antes e depois da view
# (segurança, sessão, autenticação, etc)
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# CONFIGURAÇÃO DE URLs
# ============================================================
# Define qual arquivo é o ponto central das URLs do projeto
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#root-urlconf
ROOT_URLCONF = 'CrudBasico.urls'


# ============================================================
# TEMPLATES
# ============================================================
# Configura o mecanismo de templates do Django
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Diretórios adicionais de templates (opcional)
        'DIRS': [],

        # Permite que o Django procure templates dentro dos apps
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                # Adiciona o request aos templates
                'django.template.context_processors.request',

                # Adiciona dados do usuário autenticado
                'django.contrib.auth.context_processors.auth',

                # Sistema de mensagens
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================================================
# APLICAÇÃO WSGI
# ============================================================
# Ponto de entrada para servidores web em produção
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#wsgi-application
WSGI_APPLICATION = 'CrudBasico.wsgi.application'


# ============================================================
# BANCO DE DADOS
# ============================================================
# Configuração do banco de dados
# SQLite é usado por padrão em projetos de estudo
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================================================
# VALIDAÇÃO DE SENHAS
# ============================================================
# Regras de segurança para criação de senhas
# Documentação:
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ============================================================
# INTERNACIONALIZAÇÃO
# ============================================================
# Configura idioma e fuso horário do projeto
# Documentação:
# https://docs.djangoproject.com/en/6.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ============================================================
# ARQUIVOS ESTÁTICOS
# ============================================================
# Configuração de CSS, JavaScript e imagens
# Documentação:
# https://docs.djangoproject.com/en/6.0/howto/static-files/
STATIC_URL = 'static/'

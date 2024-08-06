💻 Preparando o ambiente de trabalho:

#1. Criar o diretório do projeto:
md d:\Dev\Python\backend-django

#2. Criar um ambiente virtual:
python -m venv venv

#3. Ativar o ambiente virtual:
.\venv\Scripts\activate

#4. Instalar Django:
pip install django

#5. Instalar Django REST Framework:
pip install djangorestframework

#6. Criar um novo projeto Django:
django-admin startproject restful01

#7. Entrar no diretório do projeto:
cd .\restful01\

#8.  Criar um novo aplicativo Django:
python manage.py startapp toys

## Entendendo a estrutura do projeto
Arquivo "settings.py":
    - Descrição:
        Contém todas as configurações do projeto, incluindo:
            Apps do projeto: Lista de aplicativos instalados.
            Middlewares: Camadas de processamento que acontecem antes ou depois da view.
            Databases: Configurações do banco de dados.
            URLs: Configurações de roteamento para os aplicativos.

    ✅ contém todas as configurações do projeto
-- nosso apps.
-- middlewares.
-- databases.
✅ contém as URLs para nossos apps.

## Registrando as aplicações no settings.py:
    - Adicionar aplicativos ao projeto:
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Habilita Django REST Framework
        "rest_framework",
        # Habilita Toys application
        "toys.apps.ToysConfig",
    ]

## iniciando a aplicaçação
    - Rodar o servidor de desenvolvimento:
    python manage.py runserver


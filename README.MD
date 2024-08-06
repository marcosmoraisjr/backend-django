# Backend Django Project

Este é o repositório do projeto backend desenvolvido em Django para a CEPEDI.

## Estrutura do Projeto

```plaintext
backend-django/
├── backend_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── ...
├── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── ...
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```
## Configuração do Ambiente
# Requisitos
- Python 3.8+
- Django 3.x.x
- Virtualenv
# Passos para Configuração
1. Clone o repositório:
```
git clone https://github.com/marcosmoraisjr/backend-django.git
cd backend-django
```
2. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate   # No Windows use: venv\\Scripts\\activate
```
3. Instale as dependências:
```
pip install -r requirements.txt
```
4. Configure o banco de dados (SQLite por padrão):
```
python manage.py migrate
```
5. Crie um superusuário para acessar o admin:
```
python manage.py createsuperuser
```
6. Inicie o servidor de desenvolvimento:
```
cd .\restful01\
python manage.py runserver
```
Acesse o projeto em http://127.0.0.1:8000.

## Estrutura do Projeto
- backend_django/: Diretório do projeto Django contendo as configurações e URLs principais.
- app/: Diretório da aplicação principal contendo os modelos, visualizações, URLs e lógica de negócios.
- manage.py: Script de linha de comando para interagir com o projeto Django.
- requirements.txt: Arquivo de dependências Python necessárias para o projeto.
- README.md: Este arquivo de documentação.
- .gitignore: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.

## Como Contribuir
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
4. Faça push para a branch (git push origin feature/nova-feature).
5. Crie um novo Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato
- Marcos Morais - marcosmoraisjr@gmail.com
- GitHub: https://github.com/marcosmoraisjr


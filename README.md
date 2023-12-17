# Nunes Sports

Repositório criado para o teste da eveymind do programa de trainee bestminds, aplicação crude desenvolvida com as técnologias [Python](https://www.python.org/) com o framework de desenvolvimento web [Django](https://www.djangoproject.com/)

## Instalação

Primeiro instale o [Python 3.9+](https://www.python.org/downloads/) em sua máuina

Logo após clone o repositório em sua máquina local
```npm
git clone https://github.com/JuanTrindade/NunesSports.git
```
Em seguida inicie um ambiente virtual para instalar as depêndencias necessárias
```npm
python -m venv Venv
```
Instale as depêndencias com o Venv ativado
```npm
Venv/scripts/activate.ps1
```
```npm
pip install Django
```
Feito esses passos toda a parte de instalação de depêndencias do projeto está feito

## Inicialização

Para inicializar o projeto antes de tudo será necessário rodar as migrations para fazer a tradução do model em linguagem SQL, dentro da Pasta NunesSport digite o comando
```npm
python manage.py makemigrations
```
```npm
python manage.py migrate
```
Logo em seguida inicie o servidor local utilizando
```npm
python manage.py runserver
```

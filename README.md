
# Django Beats

Landing page do Festival Django Beats 2025


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/victorakahane/django-beats.git
```

Para melhor organização, crie e ative um ambiente virtual Python (.venv)
```bash
  python -m venv .venv
  .venv\Scripts\activate
```

Dentro do diretório do projeto, instale as dependências

```bash
  pip install -r requirements.txt
```

Entre no diretório do projeto django e execute as migrações
```bash
  cd django_beats
  python manage.py makemigrations
  python manage.py migrate
```

Inicie o servidor na porta 8000

```bash
  python manage.py runserver
```

## Acessando a área administrativa

Dentro da pasta do projeto Django, crie um superuser

```bash
  python manage.py createsuperuser
```

Em seguida, acesse http://localhost:8000/admin/ e preencha com as credenciais.


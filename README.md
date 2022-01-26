# Premios
Curso de Django

# Git y Github
```
git init
git remote add origin git@github.com:perezgarridogilb/Premios.git
git remote -v
git pull origin master --allow-unrelated-histories
```

# Python
```
python3 --version
Python 3.8.3
python3 -m venv .env
source .env/bin/activate.fish
pip3 freeze
pip3 install django
```

# Django
```
django-admin startproject premiosplatziapp
cd premiosplatziapp/
python3 manage.py runserver
python3 manage.py startapp *
```
## Databases

Los archivos makemigrations pueden servir para replicar la estructura de la Base de Datos.

```
# Crear 0001_initial.py en el que descrube la creación de las tablas como modelos (ORM)
python3 manage.py makemigrations polls
# Tomar el archivo y ejecutarlo en SQL en la Base de Datos (ORM)
python3 manage.py migrate
```
Lo ideal es que se usen base de datos relacionales 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3/mysql/postgresql/oracle',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': *,
        'PASSWORD': *
    }
}
```
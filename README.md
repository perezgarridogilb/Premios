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
# Crear un usuario y contraseña para acceder al administrador de Django
python3 manage.py createsuperuser
python3 manage.py test *
```
## Migrations

Los archivos makemigrations pueden servir para replicar la estructura de la Base de Datos.

```
# Crear 0001_initial.py en el que descrube la creación de las tablas como modelos (ORM)
python3 manage.py makemigrations polls
# Tomar el archivo y ejecutarlo en SQL en la Base de Datos (ORM)
python3 manage.py migrate
```
Lo ideal es que se usen base de datos relacionales 

## Settings.py (Production)
```
# Aquí se usarían nuestros dominios
ALLOWED_HOSTS = ['*']
```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}
```

# Docker
## Docker comands
```
# Comandos detallados por la documentación oficial de Docker
sudo docker-compose run web django-admin startproject premiosplatziapp
sudo docker-compose run web django-admin startapp *

# Revisamos la versión de docker-compose
docker-compose --version
docker-compose version 1.29.2, build 5becea4c
# En caso de ser necesario eliminamos los contenedores
docker rm -f (docker ps -a -q)
# En caso de limpiar lo que descargamos anteriormente
docker builder prune && docker system prune -a
# Se construye el servicio
docker-compose build
# Levanta los servicios instanciados en el archivo docker-compose.yml
docker-compose up
# En caso de ser necesario entrar al bash de postgreSQL
docker exec -it carpeta_db_1 bash
# Levantar el servicio en segundo plano
docker-compose up -d
# Sigo los log (Ctrl + C ya no detiene el proceso)
docker logs -f proxy
# Se borran los contenedores creados por docker-compose
docker-compose down
# Del servicio web (el código) se aplican las migraciones en caso de presentar errores
docker-compose run web python manage.py makemigrations

# En caso de ser útiles
# Detener
docker stop premiosplatziapp_web_1
# Ejecutar
docker run premiosplatziapp_web_1
```

## Dockerfile
```
FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code
# Lo mejor es que sobre todas las cosas se instalen los requerimientos en esta capa para que no lo tenga que volver a hacer en los rebuild
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

## Docker compose 
Las versiones de docker-compose llegan a cambiar, se crean dos servicios/contenedores que se comunican entre sí mediante el uso de volúmenes.
```
version: "3.9"
   
services:
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

# PostgreSQL
```
# Comando para acceder al bash del contenedor que integra el motor de Base de Datos
docker exec -it carpeta_db_1 bash
```
## Bash
```
psql -U postgres -W
# Listar Base de Datos
\l
# Seleccionar db
\c db
# Detalle de las tablas
\dt
                   List of relations
 Schema |            Name            | Type  |  Owner
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
 public | polls_choice               | table | postgres
 public | polls_question             | table | postgres

# Describir una tabla
\d nombre_tabla
```
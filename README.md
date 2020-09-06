# CursoDjango
Curso básico del framework Django para Python
Hay que instalar Python, Pip y Django, e instalar un Entorno Virtual. 
Ver tutoriales.

# Para Activar el Entorno Virtual:
pipenv shell

# Para Arrancar el Servidor: 
pipenv run python manage.py runserver
pipenv run server (entrada en el Pipfile de la siguiente forma:
    [scripts]
    server = "python manage.py runserver"
)

# Para craer un Projecto dentro del Entorno Virtual:
 pipenv run python manage.py startapp blog
 y añadir en INSTALLED_APPS del settings.py

# Añadir en el models.py nuestras clases según modelo ER
    from django.db import models

    # Create your models here.
    class Post(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
# Se crea un registro de migración con los cambios anteriores, por seguridad, creándose los ficheros 000n_initial.py:
 pipenv run python manage.py makemigrations

# Aplicar la migración en la base de datos:
 pipenv run python manage.py migrate

# Acceso a la administración de Django
http://127.0.0.1:8000/admin/login/?next=/admin/

# Crear un usuario administrador
pipenv run python manage.py createsuperuser

# Para acceder a la línea de comandos desde Django
pipenv run python manage.py shell

# Quick setup — if you’ve done this kind of thing before

https://github.com/mira-ceti/CursoDjango.git

# …or create a new repository on the command line

echo "CursoDjango" >> README.md

git init

git add README.md

git commit -m "first commit"

git remote add origin https://github.com/mira-ceti/CursoDjango.git

git push -u origin master


# …or push an existing repository from the command line
           
git remote add origin https://github.com/mira-ceti/CursoDjango.git

git push -u origin master

# Para cambiar a un repositorio remoto (hacerlo en un terminal nuevo de Ubuntu)
nano .git/config
## Y cambiar al repositorio con sus credenciales correspondientes:
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://github.com/mira-ceti/CursoDjango.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
[user]
        name = mira-ceti
        password = *********
        email = ibellon@gmail.com

# Volver a escribir el mensaje de confirmación más reciente
## Puedes cambiar el mensaje de confirmación más reciente usando el comando git commit --amend.

1. En la línea de comando, desplázate hasta el repositorio que contiene la confirmación que deseas modificar.

2. Escribe git commit --amend y presiona Enter (Intro).

3. En tu editor de texto, edita el mensaje de confirmación y guarda la confirmación.

## Puedes agregar un coautor al agregar una introducción a la confirmación. Para obtener más información, consulta "Crear una confirmación con múltiples autores".

## Puedes crear confirmaciones en nombre de tu organización agregando una introducción al mensaje de la confirmación. Para obtener más información, consulta "Crear una confirmación en nombre de una organización"

El nuevo mensaje y la confirmación aparecerán en GitHub la próxima vez que subas un cambio.


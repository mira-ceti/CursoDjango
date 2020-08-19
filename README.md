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


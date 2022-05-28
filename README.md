# Mi primera API

## instalacion del proyecto:

    1. clonar el repositorio: https://github.com/Teoraque/tienda.git

    2. crear un entorno virtual (si esta utilizando virtualenv) : virtualenv Entorno

    3. activar el entorno virtual
        
        en windows:
            Entorno\Scripts\activate

        en linux:
            source Entorno/bin/activate
    
    4. instalar los requerimientos:

            pip install requirements.txt 

        en linux ademas debera instalar psycop2-binary

            pip install psycopg2-binary

## creacion de la base de datos

para este proyecto se utilizo postgresql
pasos para la conexion de la base de datos a django

    1. dirigirse a la base de datos de postgres y ejecutar

        create database tienda;

    2. dirigirse al archivo de settings y verificar sus credenciales

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'tienda',
                'USER': 'escribir-tu-usuaurio',
                'PASSWORD': 'escruir-tu-password',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        }

    
## ejecutar el servidor

antes de ejecutar el servidor, debemos realizar las migraciones correspondientes

    1. ejecutar en la terminal: python manage.py makemigrations

    2. ejecutar en la terminal: python manage.py migrate

creando un superusuario

    1. python manage.py createsuperuser
    2. seguir todos los pasos y apuntar el username y password que coloca, ya que lo usaremos más adelante

ahora ejecutamos el servidor:

    1. python manage.py runserver

por defecto se ejecuta en el puerto 8000, por lo que debe acceder en su navegador (si no ha cambiado el host) a :

    http://127.0.0.1:8000

## visualizalizacion de swagger

podra observar la seccion de authorizacion, en donde debera autenticarse (colocando su usuario y password) y el servidor le devolvera un token de acceso,

para poder acceder al uso de las urls, debera dirigirse a Authoriza y colocar el token brindado de la siguiente manera

    1. JWT token

# ¡ listo, ya puede usar mi api!
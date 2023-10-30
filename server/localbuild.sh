#!/bin/bash
set -o errexit

# Activa un entorno virtual de Python
py -m venv venv
source venv/bin/activate

# Instala las dependencias de tu proyecto
pip install -r requirements.txt

# Realiza las migraciones de la base de datos
python manage.py migrate

# Recolecta los archivos estáticos (si es necesario)
python manage.py collectstatic --no-input

# Inicia el servidor Gunicorn en lugar del servidor de desarrollo de Django
gunicorn <TU_APP>.wsgi

# Nota: Asegúrate de que tengas un archivo `requirements.txt` válido
# que incluya todas las dependencias necesarias para tu proyecto Django.
# Reemplaza <TU_APP> con el nombre de tu aplicación Django.

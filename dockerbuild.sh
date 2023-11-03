



$ docker-compose up -d --build
$ docker-compose exec backend python manage.py makemigrations
$ docker-compose exec backend python manage.py migrate
$ docker-compose exec backend python manage.py createsuperuser

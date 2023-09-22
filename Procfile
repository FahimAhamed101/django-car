release: python manage.py migrate

web: gunicorn carshop.wsgi --log-file -
DJANGO_SUPERUSER_PASSWORD=admin0 DJANGO_SUPERUSER_USERNAME=admin0 DJANGO_SUPERUSER_EMAIL=admin0@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim10 DJANGO_SUPERUSER_LAST_NAME=fahim10 python3.9 manage.py createsuperuser --noinput
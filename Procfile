release: python manage.py migrate

web: gunicorn --workers=3 carshop.wsgi --log-file -
# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment
pip install -r requirements.txt

# make migrations
python3.9 manage.py migrate 
python3.9 manage.py migrate sessions
python3.9 manage.py collectstatic -l --noinput
DJANGO_SUPERUSER_PASSWORD=admin10 DJANGO_SUPERUSER_USERNAME=admin10 DJANGO_SUPERUSER_EMAIL=admin10@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim10 DJANGO_SUPERUSER_LAST_NAME=fahim10 python3.9 manage.py createsuperuser --noinput
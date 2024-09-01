# now_build_staticfiles.sh

# Install Python 3.6 since it is missing in the Now build environment
python3 -m venv tutorial-env

source tutorial-env/bin/activate
pip  install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate 
python3 manage.py migrate sessions
python3 manage.py collectstatic --no-input --clear
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@gmail.com DJANGO_SUPERUSER_FIRST_NAME=fahim DJANGO_SUPERUSER_LAST_NAME=fahim python3.9 manage.py createsuperuser --noinput

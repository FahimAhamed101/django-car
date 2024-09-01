pip install -r requirements.txt
python3.10 manage.py collectstatic -l --noinput
vercel build --yes
vercel --yes
2.9.9
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'carshop',

        'USER': 'postgres',

        'PASSWORD': '1234',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}"""
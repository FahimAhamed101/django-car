pip install -r requirements.txt
python3.9 manage.py collectstatic -l --noinput
vercel build --yes
vercel --yes
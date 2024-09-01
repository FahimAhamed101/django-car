pip install -r requirements.txt
python3.10 manage.py collectstatic -l --noinput
vercel build --yes
vercel --yes
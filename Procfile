release: python manage.py migrate --fake default
web: gunicorn rossetiback.wsgi 0.0.0.0:$PORT
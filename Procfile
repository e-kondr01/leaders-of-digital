release: python manage.py migrate common 0009_auto_20201017_2103 --run-syncdb
web: gunicorn rossetiback.wsgi 0.0.0.0:$PORT
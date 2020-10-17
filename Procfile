release: python manage.py makemigrations && python manage.py migrate
web: gunicorn rossetiback.wsgi 0.0.0.0:$PORT
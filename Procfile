web: gunicorn baseapi.wsgi -w 4 --max-requests 100
worker: celery -A  baseapi worker --concurrency=8 -Ofair
beat: celery -A baseapi beat

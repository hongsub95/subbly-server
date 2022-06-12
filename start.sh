#!/bin/sh 

echo "==> Migration 파일 생성"
yes | python manage.py makemigrations --settings=config.settings.dev

echo "==> Migrate 실행"
python manage.py migrate --settings=config.settings.dev --fake-initial

echo "==> collectstatic 실행"
python manage.py collectstatic --settings=config.settings.dev --noinput -v 3

echo "==> 패키지 다운로드"
pip install -r /code/requirements.txt

echo "==> 배포!"
gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=test_page.settings test_page.wsgi:application
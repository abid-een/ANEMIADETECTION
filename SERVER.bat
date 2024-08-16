cd\
cd C:\project 4\ANEMIADETECTION\ANEMIADETECTION
python manage.py makemigrations
python manage.py migrate
start "http://localhost:8000/"
python manage.py runserver
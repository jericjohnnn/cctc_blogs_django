web: gunicorn cctc_blogs_django.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn cctc_blogs_django.wsgi
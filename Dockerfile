FROM python:3.4.5
MAINTAINER Vicky Lee <vicky@twomeylee.name>

COPY manage.py manage.py
COPY requirements.txt requirements.txt
COPY migrate_posts migrate_posts
COPY mymarkdown mymarkdown
COPY news news
COPY templates templates
COPY events events
COPY codinggrace_django codinggrace_django
COPY static static

RUN pip install -r requirements.txt \
    && python manage.py test --settings=codinggrace_django.settings

EXPOSE 8000
CMD ["gunicorn", "codinggrace_django.wsgi", "--bind", "0.0.0.0:8000", "--log-file=-"]

FROM python:3.4.5
LABEL maintainer="vicky@twomeylee.name"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY manage.py manage.py
COPY migrate_posts migrate_posts
COPY mymarkdown mymarkdown
COPY news news
COPY templates templates
COPY events events
COPY codinggrace_django codinggrace_django
COPY static static

RUN python manage.py test --settings=codinggrace_django.settings \
    && python manage.py collectstatic --settings=codinggrace_django.settings --noinput

EXPOSE 8000
CMD ["gunicorn", "codinggrace_django.wsgi", "--bind=0.0.0.0:8000", "--log-file=-", "--error-logfile=-", "--capture-output", "-w", "2"]

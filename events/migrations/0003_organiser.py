# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, to_field='id', to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('blurb', models.TextField(null=True, blank=True)),
                ('contact_number', models.CharField(null=True, max_length=25, blank=True)),
                ('email', models.EmailField(null=True, max_length=75, blank=True)),
                ('url', models.URLField(max_length=250, blank=True)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

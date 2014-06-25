# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(null=True, max_length=250)),
                ('last_name', models.CharField(null=True, max_length=250)),
                ('blurb', models.TextField(null=True, blank=True)),
                ('url', models.URLField(null=True, max_length=250, blank=True)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=250)),
                ('url', models.URLField(null=True)),
                ('blurb', models.TextField(null=True)),
                ('what', models.CharField(null=True, max_length=250)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(null=True, max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=250)),
                ('country', models.ForeignKey(null=True, to_field='id', to='events.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

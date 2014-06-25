# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=250)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(max_length=250, blank=True)),
                ('city', models.ForeignKey(null=True, to_field='id', to='events.City')),
                ('country', models.ForeignKey(null=True, to_field='id', to='events.Country')),
                ('slug', models.SlugField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

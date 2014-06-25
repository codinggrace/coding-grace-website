# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_organiser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(null=True, to_field='id', to='events.City')),
                ('country', models.ForeignKey(null=True, to_field='id', to='events.Country')),
                ('email', models.EmailField(null=True, max_length=75)),
                ('url', models.URLField(max_length=250)),
                ('slug', models.SlugField(null=True)),
                ('organisers', models.ManyToManyField(null=True, to='events.Organiser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

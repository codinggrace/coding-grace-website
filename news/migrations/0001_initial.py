# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('published', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('author', models.ForeignKey(to_field='id', to='events.Organiser')),
                ('slug', models.SlugField()),
                ('short_description', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('event', models.ForeignKey(null=True, blank=True, to_field='id', to='events.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

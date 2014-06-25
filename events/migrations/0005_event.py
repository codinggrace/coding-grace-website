# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_description', models.TextField(null=True)),
                ('description', models.TextField()),
                ('faq', models.TextField(null=True, blank=True)),
                ('pub_datetime', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('location', models.ForeignKey(to_field='id', to='events.Location')),
                ('organiser', models.ForeignKey(to_field='id', to='events.Organiser')),
                ('cost', models.DecimalField(null=True, decimal_places=2, max_digits=6)),
                ('embed_ticket', models.TextField(null=True, blank=True)),
                ('event_url', models.URLField()),
                ('slug', models.SlugField()),
                ('level_type', models.ManyToManyField(to='events.Levels')),
                ('mentors', models.ManyToManyField(null=True, to='events.Mentor')),
                ('sponsors', models.ManyToManyField(to='events.Sponsor', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

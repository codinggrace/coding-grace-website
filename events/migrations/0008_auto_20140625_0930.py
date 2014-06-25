# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20140624_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='last_name',
            field=models.CharField(null=True, max_length=250, help_text='If not an organiser, fill in this', blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='first_name',
            field=models.CharField(null=True, max_length=250, help_text='If not an organiser, fill in this', blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='blurb',
            field=models.TextField(help_text='If not an organiser, fill in this', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='user',
            field=models.ForeignKey(help_text='Just pick this if mentor is an organiser also.', to_field='id', blank=True, null=True, to='events.Organiser'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='url',
            field=models.URLField(null=True, max_length=250, help_text='If not an organiser, fill in this', blank=True),
        ),
    ]

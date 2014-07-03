# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20140625_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='faq',
            field=models.TextField(blank=True, help_text='Markdown text. This field is optional.', null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='blurb',
            field=models.TextField(blank=True, help_text='If not an organiser, fill in this. Markdown text supported.', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, to_field='id', to='events.Location'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='blurb',
            field=models.TextField(help_text='Markdown text', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.TextField(help_text='Markdown text', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Markdown text'),
        ),
    ]

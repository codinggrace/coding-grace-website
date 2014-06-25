# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20140625_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='faq',
            field=models.TextField(help_text='Optional', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='slug',
            field=models.SlugField(null=True, help_text="Lowercase with '-' for spaces"),
        ),
    ]

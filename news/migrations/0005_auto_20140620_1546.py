# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20140620_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]

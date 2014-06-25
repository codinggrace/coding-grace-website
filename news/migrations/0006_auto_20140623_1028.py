# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20140620_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='published',
            field=models.DateTimeField(),
        ),
    ]

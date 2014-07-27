# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20140716_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_cancelled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20140623_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

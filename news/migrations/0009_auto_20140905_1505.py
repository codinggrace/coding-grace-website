# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20140727_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newspost',
            options={'ordering': ['-published']},
        ),
    ]

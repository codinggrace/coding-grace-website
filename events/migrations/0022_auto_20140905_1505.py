# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_event_is_cancelled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_datetime']},
        ),
        migrations.AlterModelOptions(
            name='mentor',
            options={'ordering': ['slug']},
        ),
        migrations.AddField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='user',
            field=models.ForeignKey(to_field='id', null=True, to='events.Organiser', blank=True),
            preserve_default=True,
        ),
    ]

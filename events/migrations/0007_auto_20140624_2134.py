# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_mentor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

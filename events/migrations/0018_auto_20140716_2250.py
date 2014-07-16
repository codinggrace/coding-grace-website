# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20140716_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sponsorship',
            field=models.ManyToManyField(to='events.Sponsorship'),
        ),
    ]

# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newspost_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='location',
            field=models.ForeignKey(null=True, to='events.City', to_field='id'),
        ),
    ]

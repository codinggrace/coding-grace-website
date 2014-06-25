# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='location',
            field=models.ForeignKey(to_field='id', to='events.Location', null=True),
            preserve_default=True,
        ),
    ]

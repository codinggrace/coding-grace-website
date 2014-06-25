# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20140620_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='chapter',
            field=models.ForeignKey(null=True, to_field='id', to='events.Chapter'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='location',
        ),
    ]

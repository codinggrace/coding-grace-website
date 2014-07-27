# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_newspost_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, to='events.Chapter', to_field='id'),
        ),
    ]

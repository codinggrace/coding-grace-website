# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20140625_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(null=True, decimal_places=2, help_text='E.G. 10.00', max_digits=6),
        ),
    ]

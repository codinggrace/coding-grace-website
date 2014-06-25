# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20140625_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='user',
            field=models.ForeignKey(to_field='id', null=True, blank=True, to='events.Organiser', help_text='Only choos this if mentor is an organiser also. No need to fill rest of form.'),
        ),
    ]

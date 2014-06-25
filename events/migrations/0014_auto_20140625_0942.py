# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20140625_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='embed_ticket',
            field=models.TextField(blank=True, null=True, help_text='Just paste in the html embed ticket, or just place instructions in HTML/Markdown here to display in ticket section.'),
        ),
    ]

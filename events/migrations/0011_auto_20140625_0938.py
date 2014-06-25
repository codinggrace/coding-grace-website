# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20140625_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(null=True, help_text='E.G. some-building-dublin'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='slug',
            field=models.SlugField(null=True, help_text='E.G. firstname-lastname'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='slug',
            field=models.SlugField(null=True, help_text='E.G. microsoft-ireland'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(null=True, help_text='E.G. dublin'),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='slug',
            field=models.SlugField(null=True, help_text='E.G. firstname-lastname'),
        ),
    ]

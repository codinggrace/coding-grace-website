# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20140703_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sponsor', models.ForeignKey(to_field='id', to='events.Sponsor', null=True)),
                ('sponsorship_type', models.CharField(max_length=250, help_text='E.G. Food', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsorship',
            field=models.ManyToManyField(blank=True, to='events.Sponsorship'),
            preserve_default=True,
        ),
    ]

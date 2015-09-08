# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soul',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='имя', unique=True)),
                ('key', models.CharField(max_length=200, verbose_name='key', blank=True)),
                ('kind', models.CharField(max_length=2, choices=[('OW', 'Master'), ('PM', 'Slave'), ('CL', 'Cadger')])),
                ('reg_data', models.DateTimeField(auto_now_add=True, verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Swag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='имя', unique=True)),
                ('cost', models.IntegerField(default=0, verbose_name='cost')),
                ('take_data', models.DateTimeField(auto_now_add=True, verbose_name='date came')),
                ('owner', models.ForeignKey(to='pawnshop.Soul')),
            ],
        ),
    ]

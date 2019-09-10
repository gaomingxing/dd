# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=20)),
                ('age', models.CharField(default=b'', max_length=20)),
                ('gender', models.CharField(default='\u7537', max_length=10)),
                ('addr', models.CharField(default=b'', max_length=20)),
                ('height', models.CharField(default=b'', max_length=20)),
                ('is_delete', models.BooleanField(default=0)),
            ],
        ),
    ]

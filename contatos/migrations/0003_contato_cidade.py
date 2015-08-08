# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='cidade',
            field=models.CharField(max_length=50, default='Teresina'),
        ),
    ]

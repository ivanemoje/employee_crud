# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20181112_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='song',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='song',
            name='singer',
        ),
        migrations.AddField(
            model_name='song',
            name='department',
            field=models.CharField(max_length=25, default='IT', choices=[('IT', 'IT'), ('Legal', 'Legal'), ('Finance', 'Finance'), ('Engineering', 'Engineering'), ('HR', 'HR')]),
        ),
        migrations.AddField(
            model_name='song',
            name='email',
            field=models.EmailField(max_length=254, blank=True, default=''),
        ),
        migrations.AddField(
            model_name='song',
            name='nationality',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]

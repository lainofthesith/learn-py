# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-08 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='name',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='description',
            new_name='blockquote',
        ),
        migrations.AddField(
            model_name='quote',
            name='source',
            field=models.URLField(default='https://www.goodreads.com/quotes', max_length=220),
            preserve_default=False,
        ),
    ]
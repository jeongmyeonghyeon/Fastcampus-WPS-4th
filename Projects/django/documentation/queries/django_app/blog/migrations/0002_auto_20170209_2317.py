# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Post',
        ),
    ]

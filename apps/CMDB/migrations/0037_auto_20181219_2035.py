# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-19 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0036_auto_20181213_1404'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='networkcard_assets',
            unique_together=set([('host', 'macaddress', 'ip')]),
        ),
    ]
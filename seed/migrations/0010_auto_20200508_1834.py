# Generated by Django 3.0.5 on 2020-05-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0009_auto_20200508_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countryplc',
            old_name='global_plc',
            new_name='variety',
        ),
    ]

# Generated by Django 2.2 on 2020-04-06 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0025_remove_variety_plc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='varietysupplier',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='varietysupplier',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='varietysupplier',
            name='entity',
        ),
    ]

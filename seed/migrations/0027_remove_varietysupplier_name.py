# Generated by Django 2.2 on 2020-04-06 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0026_auto_20200406_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='varietysupplier',
            name='name',
        ),
    ]

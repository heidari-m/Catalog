# Generated by Django 2.2 on 2020-04-06 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0024_variety_global_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variety',
            name='plc',
        ),
    ]
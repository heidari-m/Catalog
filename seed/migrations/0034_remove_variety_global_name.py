# Generated by Django 2.2 on 2020-04-09 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0033_auto_20200409_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variety',
            name='global_name',
        ),
    ]

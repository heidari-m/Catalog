# Generated by Django 2.2 on 2020-04-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0039_auto_20200413_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='photo_legend',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='photo_title',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]

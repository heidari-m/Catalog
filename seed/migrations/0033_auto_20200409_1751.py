# Generated by Django 2.2 on 2020-04-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0032_auto_20200406_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='photo_legend',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='variety',
            name='photo_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
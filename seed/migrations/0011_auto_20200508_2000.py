# Generated by Django 3.0.5 on 2020-05-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0010_auto_20200508_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryplc',
            name='local_picture',
            field=models.FileField(blank=True, null=True, upload_to='seed/repo/country_plc/document'),
        ),
    ]
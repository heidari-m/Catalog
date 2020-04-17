# Generated by Django 2.2 on 2020-03-31 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0002_auto_20200331_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varietysupplier',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='seed/repo/supplier/document'),
        ),
        migrations.AlterField(
            model_name='varietysupplier',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='seed/repo/supplier/image'),
        ),
    ]

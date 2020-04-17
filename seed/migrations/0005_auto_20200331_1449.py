# Generated by Django 2.2 on 2020-03-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0004_varietybasedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='varietysupplier',
            old_name='documents',
            new_name='document',
        ),
        migrations.AddField(
            model_name='varietybasedata',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='seed/repo/Bancella/document'),
        ),
        migrations.AlterField(
            model_name='varietybasedata',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='seed/repo/Bancella/image'),
        ),
    ]
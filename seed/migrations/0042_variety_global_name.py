# Generated by Django 2.2 on 2020-04-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0041_auto_20200414_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='global_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

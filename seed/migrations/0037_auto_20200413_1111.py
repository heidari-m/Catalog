# Generated by Django 2.2 on 2020-04-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0036_auto_20200410_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='product_life_cycle',
        ),
        migrations.AlterField(
            model_name='variety',
            name='serial_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]

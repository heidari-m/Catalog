# Generated by Django 2.2 on 2020-04-06 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0031_productlifecycle_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varietybasedata',
            name='variety',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seed.Variety'),
        ),
    ]
# Generated by Django 2.2 on 2020-04-06 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0027_remove_varietysupplier_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='varietysupplier',
            name='variety',
            field=models.ForeignKey(default='SIM0AA01', on_delete=django.db.models.deletion.CASCADE, to='seed.Variety'),
            preserve_default=False,
        ),
    ]

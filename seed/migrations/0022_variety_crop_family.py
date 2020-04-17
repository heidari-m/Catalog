# Generated by Django 2.2 on 2020-04-06 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0021_remove_variety_crop_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='crop_family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seed.CropFamily'),
            preserve_default=False,
        ),
    ]

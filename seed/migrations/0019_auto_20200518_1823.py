# Generated by Django 3.0.5 on 2020-05-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0018_auto_20200517_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='germination_lasts_year_max_interval',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='germination_lasts_year_min_interval',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='seed_count_per_gramme_max_interval',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='seed_count_per_gramme_min_interval',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]

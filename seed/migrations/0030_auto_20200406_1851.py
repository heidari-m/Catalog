# Generated by Django 2.2 on 2020-04-06 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0029_auto_20200406_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='seed.ProductType'),
        ),
    ]
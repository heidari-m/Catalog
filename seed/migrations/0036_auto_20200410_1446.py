# Generated by Django 2.2 on 2020-04-10 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0035_auto_20200410_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='global_crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.GlobalCrop'),
        ),
        migrations.AlterField(
            model_name='variety',
            name='serial_no',
            field=models.CharField(error_messages={'required': 'your custom error message'}, max_length=12, primary_key=True, serialize=False),
        ),
    ]
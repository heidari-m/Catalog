# Generated by Django 2.2 on 2020-03-30 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_field', models.CharField(choices=[('s', 'seeds'), ('f2', 'field2'), ('f3', 'field3')], max_length=2)),
                ('type', models.CharField(choices=[('o', 'Open Pollinated'), ('h', 'Hybrid'), ('b', 'Both')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CropFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('business_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.BusinessDivision')),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('common_name', models.CharField(blank=True, max_length=50, null=True)),
                ('latin_name', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='seed/repo/species/image')),
                ('seed_count_per_gramme_min_interval', models.IntegerField(blank=True, null=True)),
                ('seed_count_per_gramme_max_interval', models.IntegerField(blank=True, null=True)),
                ('germination_lasts_year_min_interval', models.IntegerField(blank=True, null=True)),
                ('germination_lasts_year_max_interval', models.IntegerField(blank=True, null=True)),
                ('sow_type', models.CharField(blank=True, choices=[('d', 'DIRECT SOWING'), ('t', 'TRANSPLANT'), ('b', 'Both')], default='d', max_length=1, null=True)),
                ('direct_sowing_type', models.CharField(blank=True, choices=[('h', 'By Hand'), ('m', 'Machine')], default='h', max_length=1, null=True)),
                ('hand_type', models.CharField(blank=True, choices=[('s', 'seed by seed'), ('b', 'broadcasted')], default='s', max_length=1, null=True)),
                ('sow_KG_HA_min_interval1', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sow_KG_HA_max_interval1', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sow_transplant_min_interval', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sow_transplant_max_interval', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('depth_type', models.CharField(blank=True, choices=[('d', 'DIRECT SOWING'), ('t', 'TRANSPLANT'), ('b', 'Both')], default='d', max_length=1, null=True)),
                ('depth_min_interval', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('depth_max_interval', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('distance_CM_row_to_row_min_interval', models.IntegerField(blank=True, null=True)),
                ('distance_CM_row_to_row_max_interval', models.IntegerField(blank=True, null=True)),
                ('distance_CM_plant_to_plant_min_interval', models.IntegerField(blank=True, null=True)),
                ('distance_CM_plant_to_plant_max_interval', models.IntegerField(blank=True, null=True)),
                ('sprouting_time_days_min_interval', models.IntegerField(blank=True, null=True)),
                ('sprouting_time_days_max_interval', models.IntegerField(blank=True, null=True)),
                ('CropFamily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.CropFamily')),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('serial_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('global_name', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='seed/repo/variety/image')),
                ('crop_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.CropFamily')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.Species')),
            ],
        ),
        migrations.CreateModel(
            name='VarietyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VarietySupplier',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(upload_to='seed/repo/supplier/image')),
                ('documents', models.FileField(upload_to='seed/repo/supplier/document')),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Person')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='VarietyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(upload_to='seed/gallery/variety')),
                ('legend', models.CharField(blank=True, max_length=200, null=True)),
                ('variety', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Variety')),
            ],
        ),
        migrations.CreateModel(
            name='VarietyFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seed.VarietyField')),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seed.Variety')),
            ],
        ),
        migrations.AddField(
            model_name='variety',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.VarietySupplier'),
        ),
        migrations.CreateModel(
            name='SpeciesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(upload_to='seed/gallery')),
                ('legend', models.CharField(blank=True, max_length=200, null=True)),
                ('species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Species')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.Species')),
            ],
        ),
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('model2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seed.Model2')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalCrop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('business_division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.BusinessDivision')),
            ],
        ),
        migrations.AddField(
            model_name='cropfamily',
            name='global_crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.GlobalCrop'),
        ),
    ]

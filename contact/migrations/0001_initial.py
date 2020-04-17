# Generated by Django 2.2 on 2020-04-17 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_name', models.CharField(max_length=50)),
                ('primary_note', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('identification_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address_street', models.CharField(blank=True, help_text='Street', max_length=50, null=True)),
                ('street_number', models.CharField(blank=True, help_text='Street Number', max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('sir_name', models.CharField(max_length=50)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('link_to_Other_contact_person', models.CharField(blank=True, choices=[('r', 'Replacement'), ('rp', 'Report to'), ('m', 'Manager of'), ('pe', 'Peer of')], max_length=2, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Entity')),
                ('related_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.Person')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.ContactType'),
        ),
    ]

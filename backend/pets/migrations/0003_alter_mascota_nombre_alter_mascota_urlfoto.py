# Generated by Django 4.2.5 on 2023-11-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_mascota_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='urlfoto',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]

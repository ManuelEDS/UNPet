# Generated by Django 4.2.5 on 2023-11-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_organizacion_urlfoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]

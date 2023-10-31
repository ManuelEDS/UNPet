# Generated by Django 4.2.5 on 2023-10-31 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_publicacion_likes'),
        ('pets', '0002_mascota_publicacion_alter_mascota_especie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='publicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mascotas', to='posts.publicacion'),
        ),
    ]

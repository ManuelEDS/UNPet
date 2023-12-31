# Generated by Django 4.2.5 on 2023-11-07 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=45)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('fechapublicacion', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('n_mascotas', models.IntegerField(default=0)),
                ('n_mascotas_adoptadas', models.IntegerField(default=0)),
                ('idorganizacion', models.ForeignKey(blank=True, db_column='idorganizacion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='publicaciones_organizacion', to='accounts.organizacion')),
            ],
            options={
                'db_table': 'publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=300)),
                ('fechapublicacion', models.DateTimeField(auto_now_add=True)),
                ('autor_organizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='accounts.organizacion')),
                ('autor_persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='accounts.persona')),
                ('comentario_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='posts.comentario')),
                ('publicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='posts.publicacion')),
            ],
            options={
                'db_table': 'comentarios',
            },
        ),
    ]

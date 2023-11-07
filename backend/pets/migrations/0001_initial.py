# Generated by Django 4.2.5 on 2023-11-07 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('especie', models.CharField(max_length=45)),
                ('raza', models.CharField(max_length=45)),
                ('sexo', models.CharField(max_length=45)),
                ('fechanacimiento', models.DateField(blank=True, null=True)),
                ('urlfoto', models.CharField(max_length=700, null=True)),
                ('adoptada', models.BooleanField(default=False)),
                ('idorganizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas_organizacion', to='accounts.organizacion')),
                ('idpersona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas_persona', to='accounts.persona')),
                ('publicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mascotas', to='posts.publicacion')),
            ],
            options={
                'db_table': 'mascotas',
            },
        ),
    ]

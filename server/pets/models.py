from django.db import models

# Create your models here.

class Mascota(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField( max_length=45)  # Field name made lowercase.
    especie = models.IntegerField()  # Field name made lowercase.
    raza = models.CharField(max_length=45)  # Field name made lowercase.
    sexo = models.IntegerField()  # Field name made lowercase.
    fechanacimiento = models.DateField()  # Field name made lowercase.
    urlfoto = models.CharField( max_length=700, blank=True, null=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('accounts.Persona', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)  # Field name made lowercase.
    idorganizacion = models.ForeignKey('accounts.Organizacion', models.DO_NOTHING, db_column='id_organizacion', blank=True, null=True)  # Field name made lowercase.
    adoptada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'mascotas'
        
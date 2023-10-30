from django.db import models

# Create your models here.


class Mascota(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    fechanacimiento = models.DateField()
    urlfoto = models.CharField(max_length=700, blank=True, null=True)
    idpersona = models.ForeignKey('accounts.Persona', on_delete=models.CASCADE, related_name='mascotas_persona', blank=True, null=True)
    idorganizacion = models.ForeignKey('accounts.Organizacion', on_delete=models.CASCADE, related_name='mascotas_organizacion', blank=True, null=True)
    adoptada = models.BooleanField(default=False)
    
    # Relación con la publicación
    publicacion = models.OneToOneField('posts.Publicacion', on_delete=models.SET_NULL, null=True, blank=True, related_name='mascota')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'mascotas'
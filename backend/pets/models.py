from django.db import models

# Create your models here.


class Mascota(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    especie = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    fechanacimiento = models.DateField(null=True, blank=True)
    urlfoto = models.CharField(max_length=2048, null=True)
    idpersona = models.ForeignKey('accounts.Persona', on_delete=models.CASCADE, related_name='mascotas_persona', blank=True, null=True)
    idorganizacion = models.ForeignKey('accounts.Organizacion', on_delete=models.CASCADE, related_name='mascotas_organizacion', blank=True, null=True)
    adoptada = models.BooleanField(default=False)
    
    # Relación con la publicación
    publicacion = models.ForeignKey('posts.Publicacion', on_delete=models.SET_NULL, null=True, blank=True, related_name='mascotas')

    def __str__(self):
        return self.nombre


    class Meta:
        db_table = 'mascotas'
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Organizacion
# Create your models here.



class Publicacion(models.Model):
    idpublicacion = models.IntegerField(primary_key=True)  # Field name made lowercase.
    estado = models.CharField(max_length=45)  # Field name made lowercase.
    titulo = models.CharField( max_length=45)  # Field name made lowercase.
    descripcion = models.CharField( max_length=45)  # Field name made lowercase.
    fechapublicacion = models.CharField(max_length=45)  # Field name made lowercase.
    idorganizacion = models.ForeignKey('accounts.Organizacion', models.DO_NOTHING, related_name='Publicaciones_organizacion', db_column='idorganizacion', blank=True, null=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(get_user_model(), models.DO_NOTHING, related_name='Publicaciones_integrante_organizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'publicaciones'




class Comentario(models.Model):
    contenido = models.CharField(max_length=300)
    respuesta = models.CharField(max_length=300, blank=True, null=True)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    comentador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    respondedor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comentarios_respuesta', blank=True, null=True)
    comentador_org = models.ForeignKey('accounts.Organizacion', on_delete=models.CASCADE, db_column='idComentadorOrg', related_name='comentarios_organizacion', blank=True, null=True)
    respondedor_org = models.ForeignKey('accounts.Organizacion', on_delete=models.CASCADE, db_column='idRespondedorOrg', related_name='comentarios_respuesta_organizacion', blank=True, null=True)

    # Agrega otros campos si es necesario

    def __str__(self):
        return f'Comentario {self.id}'

    class Meta:
        db_table = 'comentarios'
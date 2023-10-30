from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Organizacion
# Create your models here.


class Publicacion(models.Model):
    id = models.IntegerField(primary_key=True, db_column='idpublicacion')
    estado = models.CharField(max_length=45)
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fechapublicacion = models.DateTimeField(max_length=45)
    idorganizacion = models.ForeignKey('accounts.Organizacion', models.DO_NOTHING, related_name='publicaciones_organizacion', db_column='idorganizacion', blank=True, null=True)
    idpersona = models.ForeignKey('accounts.Persona', models.DO_NOTHING, related_name='publicaciones_integrante_organizacion', blank=True, null=True)

    # Relación con los comentarios
    comentarios = models.ManyToManyField('Comentario', related_name='publicaciones_comentarios')

    def es_dueno(self, persona):
        return self.idpersona == persona

    def puede_responder(self, persona):
        return self.es_dueno(persona)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicaciones'

class Comentario(models.Model):
    contenido = models.CharField(max_length=300)
    es_respuesta = models.BooleanField(default=False)
    publicaciones = models.ManyToManyField('Publicacion', related_name='comentarios_publicaciones')
    comentador = models.ForeignKey('accounts.Persona', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    comentador_org = models.ForeignKey('accounts.Organizacion', on_delete=models.CASCADE, db_column='idComentadorOrg', related_name='comentarios_organizacion', blank=True, null=True)
    comentario_padre = models.ForeignKey('self', on_delete=models.CASCADE, related_name='respuestas', blank=True, null=True)

    # Agrega otros campos si es necesario, como fecha y hora del comentario

    def __str__(self):
        return f'Comentario {self.id}'

    class Meta:
        db_table = 'comentarios'
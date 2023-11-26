from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User
from accounts.models import Organizacion
# Create your models here.
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Campos para la relación genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Publicacion(models.Model):
    idorganizacion = models.ForeignKey('accounts.Organizacion', models.DO_NOTHING, related_name='publicaciones_organizacion', db_column='idorganizacion', blank=True, null=True)
    estado = models.CharField(max_length=45)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    fechapublicacion = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    n_mascotas = models.IntegerField(default=0)
    n_mascotas_adoptadas = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicaciones'


# id organizaciones: [24 - 29] | is personas: [1 - 23]
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    contenido = models.CharField(max_length=300)
    publicacion = models.ForeignKey(
        Publicacion, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    comentario_padre = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='respuestas', blank=True, null=True)
    fechapublicacion = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def get_autor(self):
        return self.autor

    def __str__(self):
        if self.comentario_padre:
            return f'{self.get_autor().username}: @{self.comentario_padre.get_autor().username} "{self.contenido}"'
        else:
            return f'{self.get_autor().username}: "{self.contenido}"'

    class Meta:
        db_table = 'comentarios'

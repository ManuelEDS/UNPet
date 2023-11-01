from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Organizacion
# Create your models here.


class Publicacion(models.Model):
    id = models.IntegerField(primary_key=True, db_column='idpublicacion')
    idorganizacion = models.ForeignKey('accounts.Organizacion', models.DO_NOTHING, related_name='publicaciones_organizacion', db_column='idorganizacion', blank=True, null=True)
    estado = models.CharField(max_length=45)
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fechapublicacion = models.DateTimeField(max_length=45)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicaciones'


class Comentario(models.Model):
    autor_persona = models.ForeignKey('accounts.Persona', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    autor_organizacion = models.ForeignKey('accounts.Organizacion', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    contenido = models.CharField(max_length=300)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    comentario_padre = models.ForeignKey('self', on_delete=models.CASCADE, related_name='respuestas', blank=True, null=True)
    fechapublicacion = models.DateTimeField(max_length=45)

    def get_autor(self):
        if self.autor_persona:
            return self.autor_persona
        elif self.autor_organizacion:
            return self.autor_organizacion
        else:
            return None
        
    def __str__(self):
            if self.comentario_padre:
                return f'{self.getAutor().username}: @{self.comentario_padre.getAutor().username} "{self.contenido}"'
            else:
                return f'{self.getAutor().username}: "{self.contenido}"'
            
    class Meta:
        db_table = 'comentarios'
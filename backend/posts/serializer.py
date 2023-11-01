from rest_framework import serializers
from pets.serializer import MascotaSerializer
from .models import Publicacion, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    autor = serializers.SerializerMethodField()
    respuestas = serializers.SerializerMethodField()

    class Meta:
        model = Comentario
        fields = ['id', 'contenido', 'autor', 'publicacion', 'comentario_padre', 'respuestas', 'fechapublicacion']
        read_only_fields = ['id', 'fechapublicacion']

    def get_autor(self, obj):
        return str(obj.get_autor())

    def get_respuestas(self, obj):
        if obj.respuestas.exists():
            return ComentarioSerializer(obj.respuestas.all(), many=True).data
        return None

class PublicacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    organizacion = serializers.StringRelatedField()
    mascotas = MascotaSerializer(many=True, read_only=True)

    class Meta:
        model = Publicacion
        fields = ['id', 'contenido', 'organizacion', 'comentarios', 'mascotas']






























# class ComentarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comentario
#         fields = ['id', 'contenido', 'es_respuesta', 'publicaciones', 'comentador', 'comentador_org', 'comentario_padre']
#         read_only_fields = ['id']

# class PublicacionSerializer(serializers.ModelSerializer):
#     comentarios = ComentarioSerializer(many=True, read_only=True)
#     mascotas  = MascotaSerializer(many=True, read_only=True)

#     class Meta:
#         model = Publicacion
#         fields = ['id', 'estado', 'titulo', 'descripcion', 'fechapublicacion', 'idorganizacion', 'idpersona', 'likes', 'comentarios', 'mascotas']
#         read_only_fields = ['id', 'fechapublicacion']

# class PublicacionCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publicacion
#         fields = ['estado', 'titulo', 'descripcion', 'idorganizacion', 'idpersona']

#     def create(self, validated_data):
#         publicacion = Publicacion.objects.create(**validated_data)
#         return publicacion

# class PublicacionUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publicacion
#         fields = ['estado', 'titulo', 'descripcion', 'idorganizacion', 'idpersona']

#     def update(self, instance, validated_data):
#         user = self.context['request'].user
#         if user:
#             instance.estado = validated_data.get('estado', instance.estado)
#             instance.titulo = validated_data.get('titulo', instance.titulo)
#             instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#             instance.idorganizacion = validated_data.get('idorganizacion', instance.idorganizacion)
#             instance.idpersona = validated_data.get('idpersona', instance.idpersona)
#             instance.save()
#             return instance
#         else:
#             raise serializers.ValidationError("No tienes permiso para editar esta publicación.")
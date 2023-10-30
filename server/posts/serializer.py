from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Publicacion, Comentario
from rest_framework import serializers

class PublicacionSerializer(serializers.ModelSerializer):
    Comentarios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Publicacion
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'Comentarios']
        read_only_fields = ['created_at', 'updated_at']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'Publicacion', 'author', 'content', 'created_at']
        read_only_fields = ['created_at']

class PublicacionDetailSerializer(PublicacionSerializer):
    Comentarios = ComentarioSerializer(many=True, read_only=True)

class PublicacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['title', 'content', 'author']
        read_only_fields = ['author']

    def create(self, validated_data):
        Publicacion = Publicacion.objects.create(**validated_data)
        return Publicacion

class PublicacionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['title', 'content', 'author']
        read_only_fields = ['author']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.groups.filter(name='Organizacion').exists():
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("No tienes permiso para editar esta publicación.")

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'Publicacion', 'author', 'content', 'created_at']
        read_only_fields = ['created_at']

class PublicacionDetailSerializer(PublicacionSerializer):
    Comentarios = ComentarioSerializer(many=True, read_only=True)

class PublicacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['title', 'content', 'author']
        read_only_fields = ['author']

    def create(self, validated_data):
        Publicacion = Publicacion.objects.create(**validated_data)
        return Publicacion

class PublicacionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['title', 'content', 'author']
        read_only_fields = ['author']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.groups.filter(name='Organizacion').exists():
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("No tienes permiso para editar esta publicación.")
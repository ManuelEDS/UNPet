from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Persona, Organizacion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Modifica la representación aquí
        representation['userType'] = instance.get_rol_name()
        return representation


class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',)


class OrganizacionSerializer(serializers.ModelSerializer):
    localidad = serializers.CharField(source='idlocalidad.nombre', read_only=True)
    class Meta:
        model = Organizacion
        exclude = ('id',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Agrega el nombre de la localidad a la representación
        representation['localidad'] = instance.idlocalidad.nombre
        representation['userType'] = instance.__class__.__name__
        return representation



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)

class PersonaSerializer(serializers.ModelSerializer):
    localidad = serializers.CharField(source='idlocalidad.nombre', read_only=True)

    class Meta:
        model = Persona
        exclude = ('id',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Agrega el nombre de la localidad a la representación
        representation['localidad'] = instance.idlocalidad.nombre
        representation['userType'] = instance.__class__.__name__
        return representation

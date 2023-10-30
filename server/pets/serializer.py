from rest_framework import serializers
from .models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    """
    Serializer para mostrar y listar mascotas.

    Este serializer se utiliza para representar y listar mascotas en la API.

    Campos incluidos:
    - Todos los campos del modelo Mascota.

    """
    class Meta:
        model = Mascota
        fields = '__all__'

class MascotaUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para crear, actualizar mascotas existentes.

    Este serializer se utiliza para crear, actualizar mascotas existentes y verifica si el usuario es una organización antes de permitir la actualización.

    Campos incluidos:
    - Todos los campos del modelo Mascota.

    """
    class Meta:
        model = Mascota
        fields = '__all__'

    def update(self, instance, validated_data):
        # Solo las organizaciones pueden editar mascotas
        user = self.context['request'].user
        if user.groups.filter(name='Organizacion').exists():
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("No tienes permisos para editar esta mascota.")

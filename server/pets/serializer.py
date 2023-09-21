from rest_framework import serializers
from .models import Pets


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'
        # para serializar todo: fields = '__all__'

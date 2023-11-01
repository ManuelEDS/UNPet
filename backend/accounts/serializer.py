from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Organizacion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',)


class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)


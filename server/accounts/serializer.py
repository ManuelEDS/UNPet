from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import User, Organitation

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OrganitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organitation
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=50)
    n_doc = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    phoneNumber = serializers.CharField(max_length=20)

    class Meta:
        model = User
        exclude = ("id",)

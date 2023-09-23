from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import User
from . import re
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'username')
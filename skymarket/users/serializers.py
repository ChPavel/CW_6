from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    pass


class CurrentUserSerializer(serializers.ModelSerializer):
    pass


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор
    """
    class Meta:
        model = User
        fields = '__all__'

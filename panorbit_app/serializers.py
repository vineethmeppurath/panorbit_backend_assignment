from random import random

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate_email(self, value: str) -> str:
        """function to validate email

        Args:
            value: email
        Return:
            value: email
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    class Meta:
        model = User
        fields = ('first_name', 'last_name','gender', 'email', 'phone_number')

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
        )
        return user



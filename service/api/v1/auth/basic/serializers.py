from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

from apps.user.models import User


class BasicSignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User

        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )

    @staticmethod
    def validate_password(value):
        try:
            password_validation.validate_password(value)
        except ValidationError as error:
            raise serializers.ValidationError(
                error.messages
            )

        return value

    @transaction.atomic()
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class BasicSignInSerializer(TokenObtainPairSerializer):
    pass

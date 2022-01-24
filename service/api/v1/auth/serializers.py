from rest_framework import serializers
from django.db import transaction
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from apps.user.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

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

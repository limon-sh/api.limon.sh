import factory
import pytest
from rest_framework import exceptions

from api.v1.auth.serializers import SignUpSerializer
from apps.user.models import User


@pytest.mark.django_db
class TestSignUpSerializer:
    @pytest.mark.parametrize('password', [
        'qwerty12',
        '12345678'
    ])
    def test_validate_password(self, password):
        with pytest.raises(exceptions.ValidationError):
            assert SignUpSerializer.validate_password(password)

    def test_create_user_after_sign_up(self, user_factory):
        serializer = SignUpSerializer(
            data=factory.build(dict, FACTORY_CLASS=user_factory)
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        assert User.objects.exists()

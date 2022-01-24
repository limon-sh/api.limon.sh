import pytest
from rest_framework import exceptions

from api.v1.auth.serializers import SignUpSerializer


class TestSignUpSerializer:
    @pytest.mark.parametrize('password', [
        'qwerty12',
        '12345678'
    ])
    def test_validate_password(self, password):
        with pytest.raises(exceptions.ValidationError):
            assert SignUpSerializer.validate_password(password)

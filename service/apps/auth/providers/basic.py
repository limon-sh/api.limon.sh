from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.auth.providers import AuthenticationProvider
from apps.user.models import User


class BasicAuthenticationProvider(AuthenticationProvider):
    @classmethod
    def sign_up(cls, request) -> RefreshToken:

        user = User.objects.create_user(
            email=request.data.get('email'),
            password=request.data.get('password'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name')
        )
        return RefreshToken.for_user(user)

    @classmethod
    def sign_in(cls, request) -> RefreshToken:
        try:
            return RefreshToken.for_user(
                User.objects.get(
                    email=request.data.get('email')
                )
            )
        except User.DoesNotExist:
            raise ValidationError("User doesn't exists")

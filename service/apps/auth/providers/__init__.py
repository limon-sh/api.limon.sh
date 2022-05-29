from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationProvider:
    @classmethod
    def sign_up(cls, request: Request) -> RefreshToken:
        raise NotImplementedError()

    @classmethod
    def sign_in(cls, request: Request) -> RefreshToken:
        raise NotImplementedError()

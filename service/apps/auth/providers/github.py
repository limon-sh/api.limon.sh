from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken

from apps.auth.providers import AuthenticationProvider


class GithubAuthenticationProvider(AuthenticationProvider):
    @classmethod
    def sign_up(cls, request: Request) -> RefreshToken:
        breakpoint()

    @classmethod
    def sign_in(cls, request: Request) -> RefreshToken:
        breakpoint()

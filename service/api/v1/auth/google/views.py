from urllib.parse import urlencode

from django.shortcuts import redirect
from rest_framework import decorators, permissions

from api.v1.auth.views import AuthenticationViewSet
from apps.auth.providers.google import GoogleAuthenticationProvider
from rest_framework.response import Response


class GoogleAuthenticationViewSet(AuthenticationViewSet):
    auth_provider = GoogleAuthenticationProvider

    @decorators.action(
        detail=False,
        name='sign-in',
        methods=['get'],
        url_path='sign-in',
        permission_classes=[
            permissions.AllowAny
        ]
    )
    def sign_in(self, request, *args, **kwargs):
        """
        Google sign-in

        Takes a set of user credentials and returns an access and
        refresh JSON web token pair to prove the authentication
        of those credentials.
        """

        return super().sign_in(request, *args, **kwargs)

    @decorators.action(
        detail=False,
        name='sign-up',
        methods=['get'],
        url_path='sign-up',
        permission_classes=[
            permissions.AllowAny
        ]
    )
    def sign_up(self, request, *args, **kwargs):
        """
        Google sign-up

        Sign up a new user and send confirmation email.
        """

        return super().sign_up(request, *args, **kwargs)

    @staticmethod
    def response(url: str, data: dict) -> Response:
        return redirect(f"{url}?{urlencode(data)}")

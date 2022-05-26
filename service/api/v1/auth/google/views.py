from urllib.parse import urlencode

from django.shortcuts import redirect
from rest_framework import viewsets, decorators, permissions

from apps.auth.google.services import GoogleAuthenticationService


class GoogleAuthenticationViewSet(viewsets.ViewSet):
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

        token = GoogleAuthenticationService.sign_up(request)

        return redirect(f"http://localhost:8081/sign-up?{urlencode({'token': token})}")

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

        token = GoogleAuthenticationService.sign_in(request)

        return redirect(f'http://localhost:8081/sign-in?access_token={token}')

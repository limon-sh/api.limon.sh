from urllib.parse import urlencode

from django.shortcuts import redirect
from rest_framework import viewsets

from apps.auth.providers import AuthenticationProvider
from apps.auth.services import AuthenticationService
from settings import (
    FRONTEND_SIGN_IN_URL,
    FRONTEND_SIGN_UP_URL
)


class AuthenticationViewSet(viewsets.ViewSet):
    auth_service = AuthenticationService
    auth_provider: AuthenticationProvider = None

    # TODO: Change on one method authenticate

    def sign_in(self, request, *args, **kwargs):
        result = self.auth_service.authenticate(
            request, getattr(self.auth_provider, 'sign_in')
        )

        if result.has_errors():
            data = {
                'errors': result.errors
            }
        else:
            data = {
                'access_token': result.access_token(),
                'refresh_token': result.refresh_token()
            }

        return self.response(FRONTEND_SIGN_UP_URL, data)

    def sign_up(self, request, *args, **kwargs):
        result = self.auth_service.authenticate(
            request, getattr(self.auth_provider, 'sign_up')
        )

        if result.has_errors():
            data = {
                'errors': result.errors
            }
        else:
            data = {
                'access_token': result.access_token(),
                'refresh_token': result.refresh_token()
            }

        return self.response(FRONTEND_SIGN_UP_URL, data)

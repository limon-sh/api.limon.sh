from typing import Callable

from rest_framework.request import Request

from apps.auth.dataclasses import AuthenticationResult


class AuthenticationService:
    @staticmethod
    def authenticate(
            request: Request,
            provider_method: Callable
    ) -> AuthenticationResult:
        try:
            return AuthenticationResult(token=provider_method(request))
        except Exception as error:
            # TODO: Make more flexible error message
            return AuthenticationResult(errors=[str(error)])

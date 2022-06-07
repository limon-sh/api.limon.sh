from rest_framework import decorators, permissions
from api.v1.auth.views import AuthenticationViewSet
from .serializers import BasicSignUpSerializer, BasicSignInSerializer
from apps.auth.providers.basic import BasicAuthenticationProvider


class BasicAuthenticationViewSet(AuthenticationViewSet):

    auth_provider = BasicAuthenticationProvider

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
        Sign up
        Sign up a new user and send confirmation email.
        """

        serializer = BasicSignUpSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        return super().sign_up(request, *args, **kwargs)

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
        Sign in
        Takes a set of user credentials and returns an access and
        refresh JSON web token pair to prove the authentication
        of those credentials.
        """

        serializer = BasicSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().sign_in(request, *args, **kwargs)

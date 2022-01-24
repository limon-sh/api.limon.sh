from rest_framework import viewsets, status, response, decorators, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from apps.user.models import User
from .serializers import SignUpSerializer


class AuthenticationViewSet(viewsets.ViewSet):
    @decorators.action(
        detail=False,
        methods=['post'],
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

        serializer = SignUpSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        refresh = RefreshToken.for_user(
            User.objects.create_user(**serializer.validated_data)
        )

        return response.Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED
        )

    @decorators.action(
        detail=False,
        methods=['post'],
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

        serializer = TokenObtainPairSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return response.Response(
            serializer.validated_data, status=status.HTTP_200_OK
        )

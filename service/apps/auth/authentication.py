from django.core.cache import caches
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

from apps.user.models import User
from apps.user.serializers import UserCacheSerializer


class JWTAuthenticationCache(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """

        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(_("Token contained no recognizable user identification"))

        try:
            user = self.get_user_instance(user_id)
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(_("User not found"), code="user_not_found")

        if not user.is_active:
            raise AuthenticationFailed(_("User is inactive"), code="user_inactive")

        return user

    def get_user_instance(self, user_id: str) -> User:
        cache = caches[settings.AUTHENTICATION_CACHE]

        if user_data := cache.get(user_id):
            return User(**user_data)

        user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})

        cache.set(
            user_id,
            UserCacheSerializer(instance=user).data,
            settings.AUTHENTICATION_CACHE_TIMEOUT
        )

        return user

from typing import Optional
from urllib.parse import urlencode

import requests
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken

from apps.auth.providers import AuthenticationProvider
from apps.user.models import User
from settings import (
    BACKEND_HOST,
    FRONTEND_SIGN_IN_URL,
    FRONTEND_SIGN_UP_URL,
    GOOGLE_OAUTH2_CLIENT_ID,
    GOOGLE_OAUTH2_CLIENT_SECRET
)


class GoogleAuthenticationProvider(AuthenticationProvider):
    GOOGLE_OAUTH2_ACCESS_TOKEN_URL = 'https://oauth2.googleapis.com/token'
    GOOGLE_OAUTH2_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

    @classmethod
    def sign_up(cls, request: Request) -> RefreshToken:
        user_info = cls.get_user_info(
            request,
            FRONTEND_SIGN_UP_URL,
            f"{BACKEND_HOST}{reverse('google-sign-up')}"
        )

        user, _ = User.objects.get_or_create(
            defaults={
                'first_name': user_info['given_name'],
                'last_name': user_info['family_name']
            },
            email=user_info['email']
        )

        return RefreshToken.for_user(user)

    @classmethod
    def sign_in(cls, request: Request) -> RefreshToken:
        user_info = cls.get_user_info(
            request,
            FRONTEND_SIGN_IN_URL,
            f"{BACKEND_HOST}{reverse('google-sign-in')}"
        )

        try:
            return RefreshToken.for_user(
                User.objects.get(
                    email=user_info['email']
                )
            )
        except User.DoesNotExist:
            raise ValidationError("User doesn't exists")

    @classmethod
    def get_user_info(
            cls,
            request: Request,
            error_redirect_url: str,
            redirect_url: str
    ) -> dict:
        code = request.query_params.get('code')
        error = request.query_params.get('error')

        if error or not code:
            return redirect(
                f"{error_redirect_url}?{urlencode({'error': error})}"
            )

        access_token = cls._get_access_token(
            code=code,
            redirect_uri=redirect_url
        )

        if not access_token:
            raise ValidationError('Error get Google access token')

        response = requests.get(
            cls.GOOGLE_OAUTH2_USER_INFO_URL,
            params={'access_token': access_token}
        )

        if not response.ok:
            raise ValidationError('Error getting user information from Google')

        return response.json()

    @classmethod
    def _get_access_token(cls, *, code: str, redirect_uri: str) -> Optional[str]:
        response = requests.post(
            cls.GOOGLE_OAUTH2_ACCESS_TOKEN_URL,
            data={
                'code': code,
                'client_id': GOOGLE_OAUTH2_CLIENT_ID,
                'client_secret': GOOGLE_OAUTH2_CLIENT_SECRET,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            }
        )

        if not response.ok:
            raise ValidationError('Error getting token from Google')

        return response.json().get('access_token')

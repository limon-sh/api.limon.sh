from typing import Optional
from urllib.parse import urlencode

import requests
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


class GoogleAuthenticationService:
    @classmethod
    def sign_up(cls, request: Request) -> str:
        code = request.query_params.get('code')
        error = request.query_params.get('error')

        backend_host = 'http://localhost:8000'
        frontend_host = 'http://localhost:8080'

        if error or not code:
            return redirect(
                f"{frontend_host}?{urlencode({'error': error})}"
            )

        redirect_uri = f"{backend_host}{reverse('google-sign-up')}"

        access_token = cls.get_access_token(code=code, redirect_uri=redirect_uri)

        if not access_token:
            # TODO: Raise ValidationError
            pass

        user_info = cls.get_user_info(access_token=access_token)
        # user_info = {
        #     'sub': '110887550190054463895',
        #     'name': 'Andrey Kliatsko',
        #     'given_name': 'Andrey',
        #     'family_name': 'Kliatsko',
        #     'picture': 'https://lh3.googleusercontent.com/...',
        #     'email': '...',
        #     'email_verified': True,
        #     'locale': 'en',
        #     'hd': '...'
        # }

        return access_token

    @classmethod
    def sign_in(cls, request: Request) -> str:
        return ''

    @staticmethod
    def get_access_token(*, code: str, redirect_uri: str) -> Optional[str]:
        response = requests.post(
            GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data={
                'code': code,
                'client_id': '',  # settings.GOOGLE_OAUTH2_CLIENT_ID,
                'client_secret': '',  # settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                'redirect_uri': redirect_uri,
                'grant_type': 'authorization_code'
            }
        )

        if not response.ok:
            raise ValidationError('Failed to obtain access token from Google.')

        return response.json().get('access_token')

    @staticmethod
    def get_user_info(*, access_token: str) -> dict:
        response = requests.get(
            GOOGLE_USER_INFO_URL,
            params={'access_token': access_token}
        )

        if not response.ok:
            raise ValidationError('Failed to obtain user info from Google.')

        return response.json()

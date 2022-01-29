import factory
import pytest
from rest_framework import status


@pytest.mark.django_db
class TestAuthenticationViewSet:
    def test_sign_up_response_status(self, client, user_factory):
        assert client.post(
            '/v1/auth/token/sign-up/', data=factory.build(
                dict, FACTORY_CLASS=user_factory
            )
        ).status_code == status.HTTP_201_CREATED

    def test_sign_in_response_status(self, client, user):
        assert client.post(
            '/v1/auth/token/sign-in/', data={
                'email': user.email,
                'password': user._password
            }
        ).status_code == status.HTTP_201_CREATED

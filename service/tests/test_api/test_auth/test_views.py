import pytest
from rest_framework import status


@pytest.mark.django_db
class TestAuthenticationViewSet:
    def test_sign_up_response_status(self, client, user_factory):
        user = user_factory.build()
        assert client.post(
            '/v1/auth/sign-up/', data={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password
            }
        ).status_code == status.HTTP_201_CREATED

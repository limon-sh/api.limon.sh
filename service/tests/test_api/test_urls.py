from rest_framework import status


class TestUrls:
    def test_healthcheck(self, client):
        assert client.get('/healthcheck/').status_code == status.HTTP_200_OK

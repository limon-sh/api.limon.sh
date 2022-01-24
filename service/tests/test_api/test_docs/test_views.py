from rest_framework import status


class TestDocs:
    def test_docs(self, client):
        assert client.get('/v1/docs/').status_code == status.HTTP_200_OK

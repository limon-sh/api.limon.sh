import pytest


@pytest.mark.django_db
class TestPersonMixin:
    def test_name(self, user):
        assert f'{user.first_name} {user.last_name}' == user.name

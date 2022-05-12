import pytest
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

from apps.user.models import User


@pytest.mark.django_db
class TestUserModel:
    def test_unique_email(self, user_factory):
        with pytest.raises(ValidationError):
            user_factory.create_batch(2, email='duplicate@email.com')

    def test_repr(self, user):
        assert user.email == str(user)


@pytest.mark.django_db
class TestUserManager:
    @pytest.mark.parametrize('data', [
        {'is_staff': True},
        {'is_superuser': True}
    ])
    def test_create_user_with_incompatible_fields(self, data):
        with pytest.raises(ValueError):
            User.objects.create_user(**data)

    @pytest.mark.parametrize('data', [
        {'is_staff': False},
        {'is_superuser': False}
    ])
    def test_create_superuser_with_incompatible_fields(self, data):
        with pytest.raises(ValueError):
            User.objects.create_superuser(**data)

    @pytest.mark.parametrize('data', [
        {'email': None, 'password': 'pass'},
        {'email': 'email', 'password': None}
    ])
    def test_create_user_without_required_fields(self, data):
        with pytest.raises(ValueError):
            User.objects.create_superuser(**data)

    @pytest.mark.parametrize('method,data', [
        (
            User.objects.create_user,
            {'first_name': 'user', 'last_name': 'user'}
        ),
        (
            User.objects.create_superuser,
            {'first_name': 'root', 'last_name': 'root'}
        )
    ])
    def test_success_create_user(self, method, data):
        method(email='test@email.com', password='password', **data)
        assert User.objects.count() == 1


@pytest.mark.django_db
class TestMemberModel:
    def test_repr(self, member):
        assert f'{member.user.email} ({member.role})' == str(member)

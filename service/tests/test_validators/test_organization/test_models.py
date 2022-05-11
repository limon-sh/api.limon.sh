import pytest
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient
from tests.factories.user import UserFactory, MemberFactory


@pytest.mark.django_db
class TestOrganizationModelValidator:

    @pytest.mark.skip
    def test_add_yourself_to_foreign_organization(self, organization):
        user = UserFactory()
        member = MemberFactory(role="Member", user=user)
        client = APIClient()
        client.force_authenticate(user=user)
        with pytest.raises(ValidationError):
            client.put(
                f'/v1/organizations/{organization.slug}/',
                data={'member': member}
            )

    @pytest.mark.skip
    def test_wrong_role_invite_member_to_organization(self, organization, authorized_client, member):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/',
                data={'member': member}
            )

    @pytest.mark.skip
    def test_wrong_role_delete_member_from_organization(self, organization, authorized_client, member):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/',
                data={'member': ''}
            )

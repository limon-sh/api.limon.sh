import pytest
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from tests.factories.user import MemberFactory


class TestTeamModelValidator:

    @pytest.mark.skip
    def test_wrong_role_update_team(self, authorized_client, organization, team):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/team/{team.slug}',
                data={'name': 'new_name'}
            )

    @pytest.mark.skip
    def test_wrong_role_add_member_to_team(self, authorized_client, organization, team):
        new_member = MemberFactory()
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/team/{team.slug}',
                data={'member': new_member}
            )

    @pytest.mark.skip
    def test_wrong_role_delete_member_from_team(self, authorized_client, organization, team):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/team/{team.slug}',
                data={'member': ''}
            )

    @pytest.mark.skip
    def test_add_member_not_consisting_organization(self, member_factory, user, organization, team):
        member = member_factory(role="Owner", user=user)
        client = APIClient()
        client.force_authenticate(user=user)
        organization.invite(member)
        new_member = member_factory
        with pytest.raises(ValidationError):
            client.put(
                f'/v1/organizations/{organization.slug}/team/{team.slug}',
                data={'member': new_member}
            )


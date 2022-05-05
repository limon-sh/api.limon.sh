import factory
import pytest
from rest_framework import status

from tests.factories.user import TeamFactory


@pytest.mark.django_db
class TestTeamApi:

    def test_team(self, api_client, organization):
        assert api_client.get(f'/v1/organizations/{organization.slug}/team/').status_code == status.HTTP_200_OK

    def test_create_new_team(self, api_client, organization):
        assert api_client.post(
            f'/v1/organizations/{organization.slug}/team/',
            data=factory.build(dict, FACTORY_CLASS=TeamFactory)
        ).status_code == status.HTTP_201_CREATED

    def test_update_team(self, api_client, team, organization):
        assert api_client.put(
            f'/v1/organizations/{organization.slug}/team/{team.slug}/',
            data=factory.build(dict, FACTORY_CLASS=TeamFactory)
        ).status_code == status.HTTP_200_OK

    def test_team_detail(self, team, api_client, organization):
        assert api_client.get(
            f'/v1/organizations/{organization.slug}/team/{team.slug}/'
        ).status_code == status.HTTP_200_OK

    def test_delete_project(self, team, api_client, organization):
        assert api_client.delete(
            f'/v1/organizations/{organization.slug}/team/{team.slug}/'
        ).status_code == status.HTTP_204_NO_CONTENT

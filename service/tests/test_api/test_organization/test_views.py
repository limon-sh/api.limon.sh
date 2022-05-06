import factory
import pytest
from rest_framework import status

from tests.factories.organization import OrganizationFactory


@pytest.mark.django_db
class TestOrganizationsApi:

    def test_organizations(self, api_client):
        assert api_client.get(
            '/v1/organizations/'
        ).status_code == status.HTTP_200_OK

    def test_create_new_organization(self, api_client):
        assert api_client.post(
            '/v1/organizations/',
            data=factory.build(dict, FACTORY_CLASS=OrganizationFactory)
        ).status_code == status.HTTP_201_CREATED

    def test_update_organization(self, api_client, organization):
        assert api_client.put(
            f'/v1/organizations/{organization.slug}/',
            data=factory.build(dict, FACTORY_CLASS=OrganizationFactory)
        ).status_code == status.HTTP_200_OK

    def test_organization_detail(self, organization, api_client):
        assert api_client.get(
            f'/v1/organizations/{organization.slug}/'
        ).status_code == status.HTTP_200_OK

    def test_delete_organization(self, organization, api_client):
        assert api_client.delete(
            f'/v1/organizations/{organization.slug}/'
        ).status_code == status.HTTP_204_NO_CONTENT

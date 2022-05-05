import factory
import pytest
from rest_framework import status

from tests.factories.project import ProjectFactory


@pytest.mark.django_db
class TestProjectApi:

    def test_project(self, api_client, organization):
        assert api_client.get(f'/v1/organizations/{organization.slug}/project/').status_code == status.HTTP_200_OK

    def test_create_new_project(self, api_client, organization):
        assert api_client.post(
            f'/v1/organizations/{organization.slug}/project/',
            data=factory.build(dict, FACTORY_CLASS=ProjectFactory)
        ).status_code == status.HTTP_201_CREATED

    def test_update_project(self, api_client, project, organization):
        assert api_client.put(
            f'/v1/organizations/{organization.slug}/project/{project.slug}/',
            data=factory.build(dict, FACTORY_CLASS=ProjectFactory)
        ).status_code == status.HTTP_200_OK

    def test_project_detail(self, project, api_client, organization):
        assert api_client.get(
            f'/v1/organizations/{organization.slug}/project/{project.slug}/'
        ).status_code == status.HTTP_200_OK

    def test_delete_project(self, project, api_client, organization):
        assert api_client.delete(
            f'/v1/organizations/{organization.slug}/project/{project.slug}/'
        ).status_code == status.HTTP_204_NO_CONTENT

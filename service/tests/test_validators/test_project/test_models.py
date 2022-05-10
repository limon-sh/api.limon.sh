import factory
import pytest
from rest_framework.exceptions import ValidationError


class TestProjectModelValidator:

    @pytest.mark.skip
    def test_wrong_role_add_project_to_organization(self, authorized_client, organization, project_factory):
        with pytest.raises(ValidationError):
            authorized_client.post(
                f'/v1/organizations/{organization.slug}/project/',
                data=factory.build(dict, FACTRORY_CLASS=project_factory)
            )

    @pytest.mark.skip
    def test_wrong_role_update_project(self, authorized_client, organization, project_factory, project):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/project/{project.slug}/',
                data=factory.build(dict, FACTRORY_CLASS=project_factory)
            )

    @pytest.mark.skip
    def test_wrong_role_delete_project_from_organization(self, authorized_client, organization, project):
        with pytest.raises(ValidationError):
            authorized_client.delete(
                f'/v1/organizations/{organization.slug}/project/{project.slug}/'
            )

    @pytest.mark.skip
    def test_wrong_role_add_team_to_project(self, authorized_client, organization, project, team):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/project/{project.slug}/',
                data={'team': team}
            )

    @pytest.mark.skip
    def test_wrong_role_delete_team_from_project(self, authorized_client, organization, project):
        with pytest.raises(ValidationError):
            authorized_client.put(
                f'/v1/organizations/{organization.slug}/project/{project.slug}/',
                data={'team': ''}
            )

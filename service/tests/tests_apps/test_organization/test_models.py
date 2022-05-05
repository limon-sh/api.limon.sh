import pytest
from django.template.defaultfilters import slugify


@pytest.mark.django_db
class TestOrganizationModel:

    def test_repr(self, organization):
        assert organization.name == str(organization)

    def test_create_default_slug(self, organization_factory):
        organization = organization_factory()
        organization.slug = slugify(organization.name)
        assert organization.slug == slugify(organization.name)

    def test_invite_new_member(self, organization, member):
        organization.invite(member)

        assert organization.members.exists()

    def test_members_count(self, organization, member_factory):
        organization.invite(member_factory())
        organization.invite(member_factory())

        assert organization.members_count == 2

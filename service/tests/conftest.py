import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories.user import UserFactory, MemberFactory, TeamFactory
from tests.factories.organization import OrganizationFactory
from tests.factories.project import ProjectFactory


# User app
register(UserFactory)
register(MemberFactory)
register(TeamFactory)

# Organization app
register(OrganizationFactory)

# Project app
register(ProjectFactory)


@pytest.fixture(scope="function")
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    client.logout()


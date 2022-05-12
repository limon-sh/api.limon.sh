import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories.user import UserFactory, MemberFactory
from tests.factories.organization import OrganizationFactory
from tests.factories.project import ProjectFactory
from tests.factories.product import ProductFactory


# User app
register(UserFactory)
register(MemberFactory)

# Organization app
register(OrganizationFactory)

# Project app
register(ProjectFactory)

# Product app
register(ProductFactory)


@pytest.fixture(scope="function")
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    yield client
    client.logout()


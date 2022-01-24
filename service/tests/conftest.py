from pytest_factoryboy import register

from tests.factories.user import UserFactory, MemberFactory
from tests.factories.organization import OrganizationFactory


# User app
register(UserFactory)
register(MemberFactory)

# Organization app
register(OrganizationFactory)

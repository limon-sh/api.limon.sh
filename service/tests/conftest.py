from pytest_factoryboy import register

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

import factory
from django.utils.text import slugify

from apps.project.models import Project, ProjectTeam


class ProjectFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    name = factory.Faker('word')
    slug = slugify(name)
    organization = factory.SubFactory('tests.factories.organization.OrganizationFactory')

    class Meta:
        model = Project


class ProjectTeamFactory(factory.django.DjangoModelFactory):
    project = factory.SubFactory(ProjectFactory)
    team = factory.SubFactory('tests.factories.user.TeamFactory')

    class Meta:
        model = ProjectTeam

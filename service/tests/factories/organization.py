import factory
from django.utils.text import slugify

from apps.organization.models import Organization, OrganizationMember


class OrganizationFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    name = factory.Faker('word')
    slug = slugify(name)

    class Meta:
        model = Organization


class OrganizationMemberFactory(factory.django.DjangoModelFactory):
    organization = factory.SubFactory(OrganizationFactory)
    member = factory.SubFactory('tests.factories.user.UserFactory')

    class Meta:
        model = OrganizationMember

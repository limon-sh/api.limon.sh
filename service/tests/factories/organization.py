import factory

from apps.organization.models import Organization, OrganizationMember


class OrganizationFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    name = factory.Faker('word')
    slug = 'slug'

    class Meta:
        model = Organization


class OrganizationMemberFactory(factory.django.DjangoModelFactory):
    organization = factory.SubFactory(OrganizationFactory)
    member = factory.SubFactory('tests.factories.user.UserFactory')

    class Meta:
        model = OrganizationMember

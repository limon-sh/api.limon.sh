import factory

from apps.organization.models import Organization


class OrganizationFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    name = factory.Faker('word')

    class Meta:
        model = Organization

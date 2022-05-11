import factory
from django.utils.text import slugify

from apps.product.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    name = factory.Faker('word')
    slug = slugify(name)
    organization = factory.SubFactory('tests.factories.organization.OrganizationFactory')

    class Meta:
        model = Product

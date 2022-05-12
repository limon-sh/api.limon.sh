import factory
from django.utils.text import slugify

from apps.project.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    uuid = factory.Faker('uuid4')
    name = factory.Faker('word')
    slug = slugify(name)
    product = factory.SubFactory('tests.factories.product.ProductFactory')

    class Meta:
        model = Project

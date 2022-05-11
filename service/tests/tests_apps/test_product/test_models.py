import pytest
from django.template.defaultfilters import slugify


@pytest.mark.django_db
class TestProductModel:
    def test_repr(self, product):
        assert product.name == str(product)

    def test_create_default_slug(self, product_factory):
        product = product_factory()
        product.slug = slugify(product.name)
        assert product.slug == slugify(product.name)

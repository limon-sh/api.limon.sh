import factory
import pytest
from rest_framework import status

from tests.factories.product import ProductFactory


@pytest.mark.django_db
class TestProductApi:

    def test_product(self, api_client, organization):
        assert api_client.get(
            f'/v1/organizations/{organization.slug}/product/'
        ).status_code == status.HTTP_200_OK

    def test_create_new_product(self, api_client, organization):
        assert api_client.post(
            f'/v1/organizations/{organization.slug}/product/',
            data=factory.build(dict, FACTORY_CLASS=ProductFactory)
        ).status_code == status.HTTP_201_CREATED

    def test_update_product(self, api_client, organization, product):
        assert api_client.put(
            f'/v1/organizations/{organization.slug}/product/{product.slug}/',
            data=factory.build(dict, FACTORY_CLASS=ProductFactory)
        ).status_code == status.HTTP_200_OK

    def test_product_detail(self, api_client, organization, product):
        assert api_client.get(
            f'/v1/organizations/{organization.slug}/product/{product.slug}/'
        ).status_code == status.HTTP_200_OK

    def test_delete_product(self, api_client, organization, product):
        assert api_client.delete(
            f'/v1/organizations/{organization.slug}/product/{product.slug}/'
        ).status_code == status.HTTP_204_NO_CONTENT

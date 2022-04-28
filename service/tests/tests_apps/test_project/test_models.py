import pytest
from django.template.defaultfilters import slugify


@pytest.mark.django_db
class TestProjectModel:
    def test_repr(self, project):
        assert project.name == str(project)

    def test_create_default_slug(self, project_factory):
        project = project_factory()
        project.slug = slugify(project.name)
        assert project.slug == slugify(project.name)

from libs.models import BaseModel
from django.db import models
from libs.mixins import ModelValidateMixin, SlugifyMixin


class Project(BaseModel, SlugifyMixin):
    validator = ModelValidateMixin()
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, null=True)
    teams = models.ManyToManyField(
        to='user.Team',
        through='project.ProjectTeam'
    )
    organization = models.ForeignKey(
        to='organization.Organization',
        on_delete=models.CASCADE,
        validators=validator.validate()
    )

    def __str__(self):
        return self.name


class ProjectTeam(BaseModel):
    projects = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )
    teams = models.ForeignKey(
        to='user.Team',
        on_delete=models.CASCADE
    )

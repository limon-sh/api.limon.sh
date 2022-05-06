from django.utils.text import slugify

from libs.models import BaseModel
from django.db import models


class Project(BaseModel):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, null=True)
    teams = models.ManyToManyField(
        to='user.Team',
        through='project.ProjectTeam'
    )
    organization = models.ForeignKey(
        to='organization.Organization',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProjectTeam(BaseModel):
    projects = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )
    teams = models.ForeignKey(
        to='user.Team',
        on_delete=models.CASCADE
    )

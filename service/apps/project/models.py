from libs.models import BaseModel
from apps.user.models import Member
from django.db import models


class Project(BaseModel):
    name = models.CharField(max_length=32)
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


class ProjectTeam(BaseModel):
    projects = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )
    teams = models.ForeignKey(
        to='user.Team',
        on_delete=models.CASCADE
    )

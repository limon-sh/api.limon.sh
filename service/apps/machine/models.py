from libs.models import BaseModel
from django.db import models


class Machine(BaseModel):
    name = models.CharField(max_length=32, null=True)
    project = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )
    cluster = models.ForeignKey(
        to='cluster.Cluster',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class ProjectMachine(BaseModel):

    project = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )
    machine = models.ForeignKey(
        to='machine.Machine',
        on_delete=models.CASCADE
    )

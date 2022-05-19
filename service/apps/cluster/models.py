from django.utils.text import slugify

from libs.models import BaseModel
from django.db import models


class Cluster(BaseModel):
    name = models.CharField(max_length=32)
    project = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        max_length=32,
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProjectCluster(BaseModel):
    project = models.ForeignKey(
        to='project.Project',
        on_delete=models.CASCADE
    )
    cluster = models.ForeignKey(
        to='cluster.Cluster',
        on_delete=models.CASCADE
    )

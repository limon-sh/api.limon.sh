from django.utils.text import slugify

from libs.models import BaseModel
from django.db import models


class Product(BaseModel):
    # do logo field

    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    organization = models.ForeignKey(
        to='organization.Organization',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

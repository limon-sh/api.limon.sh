from django.utils.text import slugify
from libs.validators import ValidateFileSize, ValidateFileExtension

from libs.models import BaseModel
from django.db import models
from settings import base as settings


class Product(BaseModel):

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    organization = models.ForeignKey(
        to='organization.Organization',
        on_delete=models.CASCADE
    )

    logo = models.ImageField(
        upload_to=settings.DEFAULT_FILE_STORAGE,
        validators=[ValidateFileSize(settings.IMAGE_UPLOAD_MAX_SIZE),
                    ValidateFileExtension(settings.ALLOWED_IMAGE_EXTENSIONS)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    uuid = models.UUIDField(
        _('unique object identifier'),
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().full_clean()
        super().save(*args, **kwargs)


class PersonMixin(models.Model):
    first_name = models.CharField(
        _('first name'),
        max_length=64
    )
    last_name = models.CharField(
        _('last name'),
        max_length=64
    )

    class Meta:
        abstract = True

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

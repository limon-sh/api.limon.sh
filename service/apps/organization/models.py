from django.db import models
from django.utils.text import slugify

from apps.user.models import Member
from libs.models import BaseModel
from settings import base as settings


class Organization(BaseModel):
    """
    Organization model.

    An organization is a structural unit that includes members and
    various teams formed from members of the organization.
    """

    name = models.CharField(
        max_length=32
    )
    slug = models.SlugField(
        max_length=32,
        null=True
    )
    members = models.ManyToManyField(
        to='user.Member',
        through='organization.OrganizationMember'
    )

    logo = models.ImageField(
        upload_to=settings.DEFAULT_FILE_STORAGE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @property
    def members_count(self) -> int:
        return self.members.count()

    def invite(self, member: Member):
        """Invite member for current organization."""

        OrganizationMember.objects.get_or_create(
            member_id=member.pk,
            organization_id=self.pk
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class OrganizationMember(BaseModel):
    """
    OrganizationMember model.

    The model through which the connection between the organization
    and the members passes. A model is needed in order to save
    the date and time of the member's joining the organization.
    """

    organization = models.ForeignKey(
        to='organization.Organization',
        on_delete=models.CASCADE
    )
    member = models.ForeignKey(
        to='user.Member',
        on_delete=models.CASCADE
    )


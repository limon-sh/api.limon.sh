from django.db import models
from django.template.defaultfilters import slugify
from libs.mixins import SlugifyMixin
from libs.models import BaseModel
from apps.user.models import Member


class Organization(BaseModel, SlugifyMixin):
    """
    Organization model.

    An organization is a structural unit that includes members and
    various teams formed from members of the organization.
    """

    name = models.CharField(
        max_length=32
    )
    slug = models.SlugField(
        max_length=32
    )
    members = models.ManyToManyField(
        to='user.Member',
        through='organization.OrganizationMember'
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

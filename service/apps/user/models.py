from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from libs.models import BaseModel, PersonMixin


class User(BaseModel, PersonMixin, AbstractBaseUser, PermissionsMixin):
    """
    User model.

    The user is a representation of a real person registered in the system.
    """

    email = models.EmailField(
        _('email address'),
        unique=True,
        max_length=128
    )
    is_active = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        )
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )

    class UserManager(BaseUserManager):
        def _create_user(self, email, password, **kwargs):
            """
            Create and save a user with the given email and password.
            """

            if not email:
                raise ValueError(_('The given email must be set'))

            if not password:
                raise ValueError(_('The given password must be set'))

            email = self.normalize_email(email)
            user = self.model(email=email, **kwargs)
            user.set_password(password)
            user.save(using=self._db)

            return user

        def create_user(self, email=None, password=None, **kwargs):
            kwargs.setdefault('is_staff', False)
            kwargs.setdefault('is_superuser', False)

            if kwargs.get('is_staff') is True:
                raise ValueError(_('User must have is_staff=False.'))

            if kwargs.get('is_superuser') is True:
                raise ValueError(_('User must have is_superuser=False.'))

            return self._create_user(email, password, **kwargs)

        def create_superuser(self, email=None, password=None, **kwargs):
            kwargs.setdefault('is_staff', True)
            kwargs.setdefault('is_superuser', True)
            kwargs.setdefault('first_name', 'root')
            kwargs.setdefault('last_name', 'root')

            if kwargs.get('is_staff') is not True:
                raise ValueError(_('Superuser must have is_staff=True.'))

            if kwargs.get('is_superuser') is not True:
                raise ValueError(_('Superuser must have is_superuser=True.'))

            return self._create_user(email, password, **kwargs)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.get_username()


class Member(BaseModel):
    """
    Member model.

    Member is an aggregate concept for several entities:
    a member of an organization and a member of a team.
    Each of these objects can have a different role.
    """

    class Role(models.TextChoices):
        MEMBER = 'Member', _('Member')
        MANAGER = 'Manager', _('Manager')
        OWNER = 'Owner', _('Owner')
        ADMIN = 'Admin', _('Admin')

    user = models.ForeignKey(
        to='user.User',
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=8,
        choices=Role.choices
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'role'),
                name='unique_member_for_user'
            )
        ]

    def __str__(self):
        return f'{self.user.email} ({self.role})'

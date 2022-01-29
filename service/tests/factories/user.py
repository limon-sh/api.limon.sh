import factory

from apps.user.models import User, Member


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('word')
    last_name = factory.Faker('word')
    email = factory.Faker('email')
    password = factory.Faker('sentence')
    is_active = True
    is_superuser = False

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Save original password for user in `_password` attribute."""

        original_password = kwargs['password']

        user = cls._get_manager(model_class).create_user(*args, **kwargs)
        user._password = original_password

        return user


class MemberFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    role = factory.Iterator(Member.Role.values)

    class Meta:
        model = Member

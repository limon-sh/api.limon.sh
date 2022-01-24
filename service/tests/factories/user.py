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


class MemberFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    role = factory.Iterator(Member.Role.values)

    class Meta:
        model = Member

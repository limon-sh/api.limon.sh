import os


class Environment:
    DEVELOP = 'develop'
    PRODUCTION = 'production'

    @classmethod
    def current(cls) -> str:
        return os.environ.get('ENVIRONMENT', cls.DEVELOP)

    @classmethod
    def is_develop(cls) -> bool:
        return cls.current() == cls.DEVELOP

    @classmethod
    def is_production(cls) -> bool:
        return cls.current() == cls.PRODUCTION


if Environment.is_develop():
    from .develop import *
elif Environment.is_production():
    from .production import *
else:
    raise ValueError('Unknown environment type')

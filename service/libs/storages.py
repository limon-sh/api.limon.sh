import os
import uuid
from settings import base as settings

from django.core.files import storage as django_storage


class UniqueFileNameStorage(django_storage.Storage):
    def get_available_name(self, name, max_length=None):
        path, filename = os.path.split(name)
        name = os.path.join(settings.UPLOAD_AVATARS_TO, str(uuid.uuid4()), filename)

        return super().get_available_name(name, max_length)


class LocalMediaStorage(UniqueFileNameStorage, django_storage.FileSystemStorage):
    pass

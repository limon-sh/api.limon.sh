from django.core.exceptions import ValidationError
import os


class ValidateFileExtension:
    def __init__(self, allowed_extensions, message=None):
        self.allowed_extensions = allowed_extensions
        self.message = message

    def __call__(self, file):
        _, ext = os.path.splitext(str(file))

        if ext.lower() not in self.allowed_extensions:
            raise ValidationError(
                self.message
                if self.message
                else f"Incorrect file format {ext}. Please select different file"
            )


class ValidateFileSize:
    def __init__(self, max_size, message=None):
        self.max_size = max_size
        self.message = message

    def __call__(self, file):
        if file.size > self.max_size:
            megabytes = self.max_size // (1024 * 1024)
            raise ValidationError(
                self.message
                if self.message
                else f"Incorrect file size. File can not be more {megabytes} MB."
            )

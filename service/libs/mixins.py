# from django.core.exceptions import ValidationError
#
#
# class ModelValidateMixin:
#     """
#     Validates model fields and returns existing errors
#     """
#
#     def clean(self, *args, **kwargs):
#         self.validate(raise_exceptions=True)
#         super().clean(*args, **kwargs)
#
#     def _get_validators(self):
#         return [
#             getattr(self, attr)
#             for attr in dir(self) if attr.startswith("validate_")
#         ]
#
#     def validate(self, raise_exceptions=False):
#         _errors = []
#
#         for validation in self._get_validators():
#             try:
#                 validation()
#             except ValidationError as error:
#                 _errors.append(error)
#
#         if _errors and raise_exceptions:
#             raise ValidationError(_errors)
#
#         return _errors

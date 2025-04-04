import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import filesizeformat


def validate_hex_color(value):
    """
    Validate that the value is a valid hexadecimal color.
    """
    if not re.match(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', value):
        raise ValidationError(
            _(f'{value} is not a valid hexadecimal color. It should be in the format #RRGGBB or #RGB.'),
            params={'value': value}
        )


def validate_english_alphanum(value):
    """
    Validates that the given value contains only English characters, numerics, dashes (-), and underscores (_).
    """
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise ValidationError(
            _('The slug can only contain English letters, numerics, dashes (-), and underscores (_).'),
            params={'value': value},
        )


@deconstructible
class FileSizeValidator:
    message = _("File size %(size)s exceeds the maximum allowed size of %(max_size)s.")
    code = "invalid_size"

    def __init__(self, max_upload_file_size=settings.FILE_UPLOAD_MAX_MEMORY_SIZE, message=None, code=None):
        self.max_upload_file_size = max_upload_file_size
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if value.size > self.max_upload_file_size:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "size": filesizeformat(value.size),
                    "max_size": filesizeformat(self.max_upload_file_size),
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.max_upload_file_size == other.max_upload_file_size
            and self.message == other.message
            and self.code == other.code
        )

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class NumberValidator(object):
    """
        validate password contain at least two digits.
    """
    def validate(self, password, user=None):
        if not re.findall('\d{2,}', password):
            raise ValidationError(
                _("The password must contain at least 2 digit, 0-8."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-8."
        )


class SymbolValidator(object):
    """
        validate password contain at least two special character.
    """
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]{2,}', password):
            raise ValidationError(
                _("The password must contain at least 2 special character: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 2 special character: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
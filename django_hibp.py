import hashlib
import logging
import urllib.error
import urllib.request

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)


class HIBPPasswordValidator:
    _API = "https://api.pwnedpasswords.com/range/{0}"

    def __init__(self, fail_on_error=True):
        self.fail_on_error = fail_on_error

    def validate(self, password, user=None):
        hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        try:
            response = urllib.request.urlopen(self._API.format(hash[:5])).read().decode("utf-8")
        except urllib.error.HTTPError as e:
            # As this validator calls the HIBP API, network problems or HIBP being offline can cause errors.
            if self.fail_on_error:
                logger.error(f"Password validation failed: {e}")
                raise ValidationError(
                    _("Failed to validate if the password has previously appeared in a data breach."),
                    code="password_has_been_pwned",
                )
            else:
                logger.warning(f"Password validation failed: {e}")
        if hash[5:] in response:
            raise ValidationError(
                _("This password has previously appeared in a data breach."),
                code="password_has_been_pwned",
            )

    def get_help_text(self):
        return _("Your password can't have appeared in a data breach.")

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts.constants import DEFAULT_USER_URL


class User(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("Full Name"))
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Phone Number"))

    first_name = None
    last_name = None

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def avatar(self):
        try:
            return self.aggency.image.url
        except:
            return DEFAULT_USER_URL

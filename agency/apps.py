from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AgencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agency'
    verbose_name = _('Agencies')

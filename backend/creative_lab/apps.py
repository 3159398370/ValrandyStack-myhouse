from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CreativeLabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'creative_lab'
    verbose_name = _('创意实验室')
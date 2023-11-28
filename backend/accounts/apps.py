import sys
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .poblarDB import poblar_db

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    def ready(self):
        if 'migrate' in sys.argv:
            post_migrate.connect(poblar_db, sender=self, dispatch_uid='migracionesGrupos')
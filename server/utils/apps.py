from django.apps import AppConfig
from firebase_admin import credentials, initialize_app

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utils'
    def ready(self):
        serviceAccount = "utils/serviceAccountKey.json"
        cred = credentials.Certificate(serviceAccount)
        app = initialize_app(cred, {'storageBucket': 'unpet-f599b.appspot.com'})

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
class User(AbstractUser):
    # Campos heredados de AbstractUser:
    # username, first_name, last_name, email, password, date_joined, is_active, is_staff, is_superuser, groups, user_permissions.
    
    # Métodos heredados de AbstractUser:
    # get_full_name(), get_short_name(), set_password(raw_password), check_password(raw_password), has_perm(perm, obj=None), has_perms(perm_list, obj=None), has_module_perms(app_label)

    # Campos del proyecto
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=255, blank=True)
    urlPhoto = models.TextField(db_column='url_photo')
    phoneNumber = models.IntegerField(max_length=20, db_column='phone_number')
    is_baned= models.BooleanField(null=False, default=False)


    # Define una función personalizada para autenticar al usuario por correo electrónico
    def authenticate_by_email(email, password):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    # Define una función personalizada para obtener al usuario por su ID
    def get_user_by_id(user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Moderator(User):

    

    pass
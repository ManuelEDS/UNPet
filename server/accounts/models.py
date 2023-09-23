from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class OrganizationManager(BaseUserManager):
    def create_Organization(self, email, password=None,  **extra_fields):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password,  **extra_fields)
        user.is_staff = True
        user.save()
        return user

class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        password=None,
        **extra_fields
    ):
        if not username:
            raise ValueError("An username is required.")
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")

        user = self.model(email=self.normalize_email(email),
        username=username,
        **extra_fields
                          )
        user.set_password(password)
        user.save()
        return user

    def create_Moderator(self, email, password=None,  **extra_fields):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password,  **extra_fields)
        user.is_staff = True
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password,  **extra_fields)
        user.is_superuser = True
        user.save()
        return user


class Organitation(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey("accounts.User", verbose_name=_("Propietario de la fundación"), on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, blank=True, null=True)
    urlPhoto = models.TextField(db_column="url_photo", null=True)
    phoneNumber = models.CharField(
        max_length=20, db_column="phone_number"
    )
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)

    # id_localidad = models.IntegerField() FK
    #
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    # Métodos necesarios para el funcionamiento del backend de autenticación
    def get_username(self):
        return self.USERNAME_FIELD

    def get_full_name(self):
        # Puedes personalizar cómo se devuelve el nombre completo
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        # Puedes personalizar cómo se devuelve el nombre corto
        return self.first_name

    def __str__(self):
        return self.username

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    n_doc = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    urlPhoto = models.TextField(db_column="url_photo", null=True)
    phoneNumber = models.CharField(
        max_length=20, db_column="phone_number"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)

    # id_localidad = models.IntegerField() FK
    #
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    # Métodos necesarios para el funcionamiento del backend de autenticación
    def get_username(self):
        return self.USERNAME_FIELD

    def get_full_name(self):
        # Puedes personalizar cómo se devuelve el nombre completo
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        # Puedes personalizar cómo se devuelve el nombre corto
        return self.first_name

    def __str__(self):
        return self.username

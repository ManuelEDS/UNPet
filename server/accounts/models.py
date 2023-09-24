from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.conf import settings

class OrganizationManager(BaseUserManager):
    def create_user(self, name, password=None,  **extra_fields):
        return self.create_Organization(name, password=None,  **extra_fields)
    def create_Organization(self, name, password=None,  **extra_fields):
        if not name:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(name, password,  **extra_fields)
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50 , unique=True)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    urlPhoto = models.TextField(db_column="url_photo", null=True)
    phoneNumber = models.CharField(
        max_length=20, db_column="phone_number"
    )
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = OrganizationManager()
    # id_localidad = models.IntegerField() FK
    #
    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ["name"," address"]

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='organitations_permissions',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='organitations_groups',
    )

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
    user_permissions = models.ManyToManyField("auth.Group", blank=True, related_name='users_permissions')
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    n_doc = models.CharField(max_length=20, null=True, unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    urlPhoto = models.TextField(db_column="url_photo", null=True)
    phoneNumber = models.CharField(
        max_length=20, db_column="phone_number", null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    objects = UserManager()

    # id_localidad = models.IntegerField() FK
    #
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='users_permissions',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='users_groups',
    )

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
        return f"{self.username}, {self.first_name}, {self.last_name}"

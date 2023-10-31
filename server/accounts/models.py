from xml.etree.ElementTree import tostring
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from pyparsing import null_debug_action

class data:
    pass
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Un nombre de usuario es requerido")
        if not email:
            raise ValueError("Un correo de usuario es requerido")
        if not password:
            raise ValueError("Una contraseña de usuario es requerida")
        user = self.model(
            email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_Moderator(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(
            email=email, username=username, password=password)
        user.is_staff = True
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        superuser = self.create_user(
            email=email, username=username, password=password,)
        superuser.is_superuser = True
        return superuser

    def create_Organization(self, email, username, nit, password=None, **extra_fields):
        from .models import Organizacion, Localidad

        if not username:
            raise ValueError("Un nombre de organizacion es requerido")
        if not password:
            raise ValueError("Una contraseña de organizacion es requerido")
        if not nit:
            raise ValueError("Un NIT de organizacion es requerido")
        if 'photo_file' in extra_fields.keys():
            extra_fields['urlfoto'] = extra_fields['photo_file']
            del extra_fields['photo_file']
        if extra_fields.get('idlocalidad') is not None:
            extra_fields['idlocalidad'] = Localidad.objects.get(idlocalidad=extra_fields['idlocalidad'])
            pass
        user = self.create_user(
            email=email, username=username, password=password,
        )
        user.groups.add(Group.objects.get(name='Organizacion'))
        org = Organizacion(
            id=user.id,
            email=email,
            username=username,
            nit=nit,
            **extra_fields,
        )

        org.save(force_insert=True)
        return user, org

    def create_Persona(self, email, username, password=None, **extra_fields):
        from .models import Persona, Localidad
        #print('estos son los datos en create persona:\n\n',email, username, password, '\n\n')

        #print('estos son los extrafields en create persona:\n\n', extra_fields.items(), '\n\n')
        if 'photo_file' in extra_fields.keys():
            extra_fields['urlfoto'] = extra_fields['photo_file']
            del extra_fields['photo_file']
        if extra_fields.get('idlocalidad') is not None:
            extra_fields['idlocalidad'] = Localidad.objects.get(idlocalidad=extra_fields['idlocalidad'])
            pass
        if not username:
            raise ValueError("Un nombre de persona es requerido")
        if not password:
            raise ValueError("Una contraseña de persona es requerido")
        user = self.create_user(
            email=email, username=username, password=password)

        user.groups.add(Group.objects.get(name='Persona'))
        p = Persona(id=user.id, email=email, username=username, **extra_fields)
        p.save(force_insert=True)
        return user, p


class Localidad(models.Model):
    idlocalidad = models.IntegerField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = "localidades"


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    objects = UserManager()
    is_superuser = models.BooleanField(default=False, db_column="es_admin")
    is_active = models.BooleanField(default=True, db_column="activada")
    is_staff = models.BooleanField(default=False, db_column="es_moderador")
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    
    # id_localidad = models.IntegerField() FK
    #
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username, email"]

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="users_permissions",
    )
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="group_users",
    )

    # Métodos necesarios para el funcionamiento del backend de autenticación
    def get_username(self):
        return self.username

    def get_rol_name(self):
        return self.get_groups()[0].name

    def get_full_name(self):
        # Puedes personalizar cómo se devuelve el nombre completo
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        # Puedes personalizar cómo se devuelve el nombre corto
        return self.first_name

    def get_groups(self):
        return [group for group in self.groups.all()]

    def __str__(self):
        return f"{self.username}"
    def toDict(self):
        return {
            "username":self.username,
            "email":self.email,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "is_superuser":self.is_superuser,
            "is_staff":self.is_staff,
            "is_active":self.is_active,
            "userType":self.get_groups()[0].name
            }

    class Meta:
        db_table = "usuarios"


class Organizacion(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, default=username)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)  # Field name made lowercase.
    nit = models.CharField(max_length=20, unique=True, db_column="nit")
    descripcion = models.CharField(
        max_length=300, blank=True, null=True
    )  # Field name made lowercase.
    telefono = models.CharField(max_length=20)  # Field name made lowercase.
    urlfoto = models.CharField(
        max_length=700, blank=True, null=True
    )  # Field name made lowercase.
    idlocalidad = models.ForeignKey(
        Localidad, models.DO_NOTHING, db_column="idlocalidad"
    )  # Field name made lowercase.
    date_joined = models.DateTimeField(
        auto_now=False, auto_now_add=True, db_column="fecha_ingreso"
    )

    objects = UserManager()
    def toDict(self):
        # print('to dict organizacion:', self.idlocalidad.nombre, type(self.idlocalidad.nombre))
        Loc=''
        idLoc =''
        if self.idlocalidad is not None:
            print('')
            Loc, idLoc=self.idlocalidad.nombre, self.idlocalidad.idlocalidad
        return {
            "username":self.username,
            "email":self.email,
            "direccion":self.direccion,
            "nit":self.nit,
            "descripcion":self.descripcion,
            "telefono":self.telefono,
            "urlfoto":self.urlfoto,
            "idlocalidad":idLoc,
            "localidad":Loc,
            "date_joined":self.date_joined,
            }
    def __str__(self):
        return f"{self.name}"
    class Meta:
        db_table = "organizaciones"


class Persona(models.Model):
    username = models.CharField(max_length=50, unique=True, db_column="nombre")
    email = models.EmailField(unique=True)
    tipo_doc = models.CharField(
        db_column="documento", max_length=5
    )  # Field name made lowercase.
    n_doc = models.CharField(
        db_column="no_documento", max_length=45
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
        # Campo de género con opciones predefinidas
    descripcion = models.CharField(
        max_length=150, blank=True, null=True
    )  # Field name made lowercase.
    telefono = models.CharField(max_length=20) # Field name made lowercase.
    urlfoto = models.CharField(
        max_length=2048, blank=True, null=True, db_column="url_foto"
    )  # Field name made lowercase.
    
    idlocalidad = models.ForeignKey(
        Localidad, models.DO_NOTHING, db_column="id_localidad"
    )  # Field name made lowercase.
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(
        auto_now=False, auto_now_add=True, db_column="fecha_ingreso"
    )

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    objects = UserManager()
    def toDict(self):
        # print('to dict persona:', self.idlocalidad.nombre, type(self.idlocalidad.nombre))
        idLoc=''
        Loc=''
        if self.idlocalidad is not None:
            Loc, idLoc=self.idlocalidad.nombre, self.idlocalidad.idlocalidad
        return {
            "username":self.username,
            "email":self.email,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "tipo_doc":self.tipo_doc,
            "n_doc":self.n_doc,
            "descripcion":self.descripcion,
            "telefono":self.telefono,
            "urlfoto":self.urlfoto,
            "idlocalidad":idLoc,
            "localidad":Loc,
            "date_joined":self.date_joined,
            
            }
    def __str__(self):
        return f"{self.username}"
    class Meta:
        db_table = "personas"


# @receiver(post_save, sender=Organizacion)
# def create_organization(sender, instance, created, **kwargs):
#     user = User.objects.get(id=instance.id)
#     if created:
#         if user.groups.filter(name='Organizacion').exists(): #True: Se creó un usuario | False: Se actualizó un usuario
#             # Agregar la persona al grupo
#             user.groups.add(Group.objects.get(name='Organizacion'))
#     else:
#         # Actualizar datos
#         username, email = instance.username, instance.email
#         if user.username != username:
#             user.username = username
#         if user.email != email:
#             user.email = email
#     user.save()




# @receiver(post_save, sender=Persona)
# def create_persona(sender, instance, created, **kwargs):
#     user = User.objects.get(id=instance.id)
#     if created:
#         print("signal - post_save de persona, if created = true")
#         # if not user.groups.filter(name='Persona').exists(): #True: Se creó un usuario | False: Se actualizó un usuario
#         #     # Agregar la persona al grupo
#         #     user.groups.add(Group.objects.get(name='Persona'))
#         pass
#     else:
#         print("signal - post_save de persona, if created = false, actualizar datos")
#         # Actualizar datos
#         username, email = instance.username, instance.email
#         if user.username != username:
#             user.username = username
#         if user.email != email:
#             user.email = email
#     user.save()



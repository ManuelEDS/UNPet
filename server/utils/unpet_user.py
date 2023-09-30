from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from accounts.models import Localidad, User
class UNPetUserManager:
    user_class =get_user_model()
    user_instance = None
    role_instance = None

    def __init__(self, user_instance=None,role_instance=None, user_id=None, **kwargs):
        if user_instance and isinstance(user_instance, self.user_class):
           if role_instance and role_instance.id == user_instance.id:
               self.role_instance = role_instance
        elif role_instance and not self.user_class.objects.filter(id=role_instance.id).exists():
            return
        elif user_id and int(user_id)>0:
            self.user_instance = self.user_class.objects.get(id=user_id)

    def crear_persona(self, **data):
        idlocalidad = data.get('idlocalidad')
        if idlocalidad:
            data['idlocalidad'] = Localidad.objects.get(id= idlocalidad)
        if data.get('idlocalidad') ==None: raise ValueError('campo idlocalidad: no existe una localidad con esa id')

        return 
    def change_password(self, old_password, new_password):
        if self.user_instance.check_password(old_password) and old_password != new_password:
            self.user_instance.set_password(raw_password=new_password)


    def save(self, rolSerializer: ModelSerializer | None):
        if rolSerializer is None:
            rolSerializer.save()
        else:
            inst_name = self.role_instance.username
            inst_email = self.role_instance.email

            if self.role_instance.objects.get(username= inst_name).id != self.role_instance.id:
                raise ValueError('Otro usuario ya tiene ese nombre de usuario (username)')

            if self.role_instance.objects.get(email= inst_email).id != self.role_instance.id:
                raise ValueError('Otro usuario ya tiene ese correo (email)')
            
            self.role_instance.save()
            self.user_instance.save()


    def is_role(self, role:str)->bool : return role in self.user_instance.get_groups()

    @property
    def get_user_instance(self): return self.user_instance

    @property
    def get_role_instance(self): return self.role_instance

    def get_roles(self): return self.user_instance.get_groups()
    
    def add_to_group(self, group:str):
        from django.contrib.auth.models import Group
        if not self.user_instance.groups.filter(name=group).exists(): #True: No existe
            # Agregar la persona al grupo
            self.user_instance.groups.add(Group.objects.get(name=group))
        self.roles = self.instance.roles


    def remove_from_group(self, group:str):
        from django.contrib.auth.models import Group
        if self.user_instance.groups.filter(name=group).exists(): #True: No existe
            # Agregar la persona al grupo
            self.user_instance.groups.remove(Group.objects.get(name=group))


from django.contrib.auth import get_user_model
from accounts.models import Localidad, Persona as p, Organizacion as org


class UNPetUserManager:
    user_class =get_user_model()
    user_instance = None
    role_instance = None
    rol=''
    def __init__(self, user_instance=None,role_instance=None, user_id=None, **kwargs):
        if user_instance is not None:
            ('paso 1')
            if role_instance is not None:
                # role_instance.refresh_from_db()
                # user_instance.refresh_from_db()
                ('paso 2')
                if role_instance.id == user_instance.id:
                    ('paso 3')
                    self.role_instance = role_instance
                    self.user_instance = user_instance
                else: raise ValueError('las instancias de usuarios no tienen la misma id, son dos usuarios completamente diferentes', user_instance.id, role_instance.id)
            else:
                ('paso 4')
                self.role_instance = self.__find_role_instance(user_instance.id)
                ('paso 5')
                self.user_instance=user_instance
        elif role_instance is not None and not self.user_class.objects.filter(id=role_instance.id).exists():
            raise ValueError(f'Ésta instancia de rol {role_instance.get_groups()[0]} no tiene un usuario asociado, es decir que no hay un usuario registrado con id = {role_instance.id}, posiblemente porque no se a aplicado el metodo save() a la instancia')
        elif user_id and int(user_id)>0:
            print('cuando solo se tiene la id es por aqui---.-.-.+')
            self.user_instance = self.user_class.objects.get(id=user_id)
            self.role_instance = self.__find_role_instance(user_id)
        else:
            print('se llega al else del constructor del unpetUserManager')
        #self.rol = self.user_instance.get_rol_name()
        #print(self.rol)

    def crear_persona(self, **data):
        idlocalidad = data.get('idlocalidad')
        if idlocalidad:
            data['idlocalidad'] = Localidad.objects.get(id= idlocalidad)
        if data.get('idlocalidad') ==None: raise ValueError('campo idlocalidad: no existe una localidad con esa id')

        return 
    def __find_role_instance(self, id):
        print('paso 1 fin role instance')
        
        if(p.objects.filter(id=id).exists()):
            return p.objects.get(id=id)
        elif(org.objects.filter(id=id).exists()):
            return org.objects.get(id=id)

    def change_password(self, old_password, new_password):
        if self.user_instance.check_password(old_password) and old_password != new_password:
            self.user_instance.set_password(raw_password=new_password)
    def toDict(self):
        return {**self.user_instance.toDict(),**self.role_instance.toDict()}

    def save(self, rolSerializer=None):
        if rolSerializer is not None:
            rolSerializer.save()
        else:
            inst_name = self.role_instance.username
            inst_email = self.role_instance.email
            rol_class = self.role_instance.__class__

            if rol_class.objects.get(username= inst_name).id != self.role_instance.id:
                raise ValueError('Otro usuario ya tiene ese nombre de usuario (username)')

            if rol_class.objects.get(email= inst_email).id != self.role_instance.id:
                raise ValueError('Otro usuario ya tiene ese correo (email)')
            
            self.role_instance.save()


    def is_role(self, role:str)->bool : 
        ('paso 2 fin role instance-- isrol()?')
        if self.user_instance is not None:
            return role in [r.name for r in self.user_instance.get_groups()]

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


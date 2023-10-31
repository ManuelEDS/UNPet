
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()
class AccountsBackend(ModelBackend):
    UserModel = get_user_model()
    def authenticate(self, request, userID=None, password=None, **kwargs):
            # Comprobar si userID es una dirección de correo electrónico
            import re
            patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if userID is None: 
                 userID= request.POST.get('username')
            print('credenciales-->', userID, password)
            if re.match(patron_correo, userID):
                # Intentar obtener el usuario por correo electrónico
                try:
                    user = User.objects.get(email=userID)
                except User.DoesNotExist:
                    return None

                # Autenticar por nombre de usuario
                user = super().authenticate(request, username=user.username, password=password)
                return user

            # Si userID no es un correo electrónico, autenticar directamente por nombre de usuario
            user = super().authenticate(request, username=userID, password=password)
            return user
    
        
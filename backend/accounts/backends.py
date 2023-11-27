import re
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class AccountsBackend(ModelBackend):
    UserModel = get_user_model()

    def authenticate(self, request, userID=None, password=None, **kwargs):
        # Comprobar si userID es una dirección de correo electrónico
        patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if userID is None: 
            userID = kwargs['username'] if 'username' in kwargs else kwargs['email']
        print('credenciales-->', userID, password)

        if re.match(patron_correo, userID):
            # Intentar obtener el usuario por correo electrónico
            try:
                user = self.UserModel.objects.get(email=userID)
                username = user.username
            except self.UserModel.DoesNotExist:
                return None
        else:
            # Si userID no es un correo electrónico, autenticar directamente por nombre de usuario
            username = userID

        # Autenticar por nombre de usuario
        return super().authenticate(request, username=username, password=password)
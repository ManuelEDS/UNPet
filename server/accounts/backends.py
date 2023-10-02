
import re
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

User = get_user_model()
class AccountsBackend(ModelBackend):
    UserModel = get_user_model()
    def authenticate(self, request, userID=None, password=None, **kwargs):
            # Comprobar si userID es una dirección de correo electrónico
            import re
            patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
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
    
    # def authenticate(self, request: HttpRequest, userID: str , password: str , **kwargs) -> AbstractBaseUser | None:
    #     user=None
    #     patron_correo= r'^[\w\.-]+@[\w\.-]+\.\w+$'
    #     try:
    #         if re.match(patron_correo, userID):
    #             print("authenticate POR CORREO:")
    #             emailUser = self.UserModel.objects.get(email=userID)
    #             # print('autheticate datos:', emailUser, userID, password )
    #             print('mas datos: email-> ', emailUser)
    #             print('mas datos: userID-> ', userID)
    #             user = super().authenticate(request, username=emailUser.get_username(), password=password)
    #             print("authenticate POR CORREO:", user)
    #         # elif userID.isdigit():
    #         #     # print("es difito, se procede a por n_doc:", userID)
    #         #     user = self.UserModel.objects.get(n_doc=userID, **kwargs)
    #         else:
    #             print("authenticate POR username:", user, userID, password)

    #             #user = self.UserModel.objects.get(username=userID, **kwargs)
    #             user = super().authenticate(request,username=userID, password=password)
    #             print("authenticate POR username:", user)
    #         if user!=None :
    #             return user if user.is_active else None
    #     except Exception as e:
    #         print('athenticate falló: ', e)
    #     return user
            
        
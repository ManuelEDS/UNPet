
import re
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest


class AccountsBackend(ModelBackend):
    UserModel = get_user_model()

    
    def authenticate(self, request: HttpRequest, userID: str , password: str , **kwargs) -> AbstractBaseUser | None:
        user=None
        patron_correo= r'^[\w\.-]+@[\w\.-]+\.\w+$'
        try:
            if re.match(patron_correo, userID):
                print("authenticate POR CORREO:")
                emailUser = self.UserModel.objects.get(email=userID)
                user = super().authenticate(request, username=emailUser.get_username(), password=password)
                print("authenticate POR CORREO:", user)
            # elif userID.isdigit():
            #     print("es difito, se procede a por n_doc:", userID)
            #     user = self.UserModel.objects.get(n_doc=userID, **kwargs)
            else:
                #user = self.UserModel.objects.get(username=userID, **kwargs)
                user = super().authenticate(request,username=userID, password=password)
                print("authenticate POR username:", user)
            if user!=None :
                return user if user.is_active else None
        except Exception as e:
            print('athenticate falló: ', e)
        return None
            
        
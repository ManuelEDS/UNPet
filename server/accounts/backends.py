
import re
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from rest_framework import exceptions


class AccountsBackend(ModelBackend):
    UserModel = get_user_model()

    
    def authenticate(self, request: HttpRequest, userID: str , password: str , **kwargs) -> AbstractBaseUser | None:
        user=None
        patron_correo= r'^[\w\.-]+@[\w\.-]+\.\w+$'
        try:
            if re.match(patron_correo, userID):
                print("authenticate POR CORREO:")
                user = self.UserModel.objects.get(email=userID)
                print("authenticate POR CORREO:", user)
            elif userID.isdigit():
                print("es difito, se procede a por n_doc:", userID)
                user = self.UserModel.objects.get(n_doc=userID)
            else:
                user = self.UserModel.objects.get(username=userID)
            if user!=None :
                return user if user.is_active else None
        except:
            pass
        return None
            
        
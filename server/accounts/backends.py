
import re
from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import _AnyUser, ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.sessions import base_session
from django.http.request import HttpRequest
from rest_framework import exceptions


class AccountsBackend(ModelBackend):
    UserModel = get_user_model()

    
    def authenticate(self, request: HttpRequest, userID: str , password: str , **kwargs) -> AbstractBaseUser | None | False:
        user=None
        patron_correo= r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron_correo, userID):
            user = super().authenticate(request, email=userID, password=password, **kwargs)
        elif userID.isdigit():
            user = self.UserModel.get(n_doc=userID)
        else:
            user = super().authenticate(request, username=userID, password=password, **kwargs)

        
        return user if user.is_active else False
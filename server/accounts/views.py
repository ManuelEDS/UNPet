from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from .serializer import UserSerializer, ProfileSerializer, OrganitationSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from rest_framework import permissions,status

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        user_email = request.data.get('email')
        username = request.data.get('username')
        user_pswd = request.data.get('password')
        extra_fields = {key: value for key, value in request.POST.items() if key not in  ['email', 'username', 'password']}
        user_model = get_user_model()
        ##
        if not username.strip():
            return Response({"details": "Ingrese un username, campo obligatorio"}, status= status.HTTP_400_BAD_REQUEST)

        ##
        if user_model.objects.filter(email=user_email).exists():
            user_obj= get_user_model().objects.get(email=user_email)
            return Response({"details": "El usuario ya existe, es el siguiente...", "user": UserSerializer(user_obj).data}, status= status.HTTP_400_BAD_REQUEST)
        ##
        user_obj = user_model.objects.create_user(email=user_email,username= username, password=user_pswd, **extra_fields)
        user_obj.save()
        user_auth = authenticate(userID=user_email, password=user_pswd, **extra_fields)
        ##
        if user_auth:
            login(request, user_auth)
            return Response({"details": "Usuario registrado con exito", "user": UserSerializer(user_obj).data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        user_ID = request.data.get('userID')
        user_pswd = request.data.get('password')
        extra_fields = {key: value for key, value in request.POST.items() if key not in  ['email', 'username', 'password']}
        ##
        if not user_ID.strip() or not user_pswd.strip():
            return Response({"details": "Ingrese un nombre de usuario o correo o numero de documento, campo obligatorio"}, status=status.HTTP_400_BAD_REQUEST)
        ##
        user_auth = authenticate(userID= user_ID, password=user_pswd, **extra_fields)
        ##
        if user_auth is not None:
            login(request, user_auth)
            user_ser= UserSerializer(user_auth).data
            print(user_ser)
            return Response({"details": "Usuario logeado con exito", "user": UserSerializer(user_auth).data}, status=status.HTTP_200_OK)
        return Response({"details": "Error en el login", "DATOS":{"user_auth": user_auth, "user_ID":user_ID, "user_pswd":user_pswd, "extra_fields":extra_fields}}, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({"details":"Algo salió mal con el cierre de sesión"},status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request, username):
        user_model = get_user_model().objects.get(username=username)
        if not user_model:
            return Response({"details": "Usuario no encontrado", "user":user_model}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"details": "Usuario encontrado", "user": UserSerializer(user_model).data}, status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        # Verifica si el usuario ha iniciado sesión

        return Response({'details': 'datos del request:', "request.user":UserSerializer(request.user).data, "request.auth":f"request.auth"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request):
        current_user = ProfileSerializer(instance=request.user,data= request.data,partial=True)
        print('USUARIO PROFILE PUT:', request.data, '====\n')
            # Valida y actualiza los campos de la instancia
        if current_user.is_valid():
            current_user.save()
            return Response({'details': 'Datos del usuario actualizados con exito','oldUserData':ProfileSerializer(request.user).data, 'newUserData':current_user.data}, status=status.HTTP_200_OK)
        else:
            return Response({'details': 'Error al actualizar los datos del usuario'}.update(current_user.errors), status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from .serializer import UserSerializer, ProfileSerializer, OrganizationSerializer
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import permissions,status
from utils.json_respond import Response
from utils.unpet_user import UNPetUserManager
from utils.firebase_manager import uploadUserIMG
from .models import Organizacion, Persona
from django.http.request import HttpRequest

class AdminRegister(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        pass



class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request:HttpRequest):
        return Response(request=request,data={"Usuarios registrados":{u.username for u in get_user_model().objects.all()},
                                                 "Organizaciones registradas":{u.username for u in Organizacion.objects.all()},
                                                 "Personas registradas":{u.username for u in Persona.objects.all()}})
    def post(self, request):
        
        user_email = request.data.get('email')
        username = request.data.get('username')
        user_pswd = request.data.get('password')

        for r in request.data:
            print(r, type(r))
        photo = request.FILES.get('photo_file')
        photo2 = request.data.get('photo_file')
        print('LA FOTO ESTÁ AQUI:-->', type(photo), photo, type(photo2), photo2)


        extra_fields = {key: value for key, value in request.data.items() if key not in  ['email', 'username', 'password']}
        user_model = get_user_model()
        ##
        if not username.strip():
            return Response(request=request, data={"data": "Ingrese un username, campo obligatorio"}, status= status.HTTP_400_BAD_REQUEST)
        ##
        if user_model.objects.filter(email=user_email).exists():
            user_obj= get_user_model().objects.get(email=user_email)
            return Response(request=request, data={"data": "El usuario con ese correo ya existe, es el siguiente...", "user": UserSerializer(user_obj).data}, status= status.HTTP_400_BAD_REQUEST)
        ##
        if user_model.objects.filter(username=username).exists():
            user_obj= get_user_model().objects.get(username=username)
            return Response(request=request, data={"data": "El usuario con ese nombre de usuario ya existe, es el siguiente...", "user": UserSerializer(user_obj).data}, status= status.HTTP_400_BAD_REQUEST)

        user_obj, rol_obj = user_model.objects.create_Persona(email=user_email,username= username, password=user_pswd, **extra_fields)
        user_auth = authenticate(request, userID=user_obj.username, password=user_pswd, **extra_fields)
        ##
        if user_auth:
            login(request, user_auth)
            if photo is not None:
                linkIMG=uploadUserIMG(foto=photo, nombre=f'user-img-{user_auth.id}')
                print('IMAGEN SUBIDA, EL LINK ES: \n\n\n', linkIMG, '\n\n\n')
            return Response(request=request, data={"data": "Usuario registrado con exito", "user": UserSerializer(user_obj).data}, status=status.HTTP_201_CREATED)

        return Response(request=request, status=status.HTTP_400_BAD_REQUEST)
    

class OrganizationRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        org_email = request.data.get('email')
        orgname = request.data.get('username')
        org_pswd = request.data.get('password')
        org_nit = request.data.get('nit')
        extra_fields = {key: value for key, value in request.data.items() if key not in  ['email', 'username', 'password']}
        user_model = get_user_model()
        ##

        if not orgname.strip():
            return Response(request=request, data={"data": "Ingrese un nombre de organizacion, campo obligatorio"}, status= status.HTTP_400_BAD_REQUEST)
    
        if not org_nit.strip():
            return Response(request=request, data={"data": "Ingrese un NIT , campo obligatorio"}, status= status.HTTP_400_BAD_REQUEST)

        ##
        if user_model.objects.filter(email=org_email).exists():
            user_obj= get_user_model().objects.get(email=org_email)
            return Response(request=request, data={"data": "El usuario ya existe, es el siguiente...", "user": UserSerializer(user_obj).data}, status= status.HTTP_400_BAD_REQUEST)
        ##
        user_obj, rol_obj = user_model.objects.create_Organization(email=org_email,username= orgname, password=org_pswd, **extra_fields)
        user_auth = authenticate(request, userID=user_obj.username, password=org_pswd, **extra_fields)
        ##
        if user_auth:
            login(request, user_auth)
            return Response(request=request, data={"data": "Usuario registrado con exito", "user": UserSerializer(user_obj).data}, status=status.HTTP_201_CREATED)
        return Response(request=request, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        if request.user.is_authenticated:
            return Response(request=request, data={"data": "Usuario ya registrado"}, status=status.HTTP_400_BAD_REQUEST)
        # print("paso 0", request.data.get("userID"))
        user_ID = request.data.get("userID")
        user_pswd = request.data.get("password")
        # print("paso 1")
        extra_fields = {key: value for key, value in request.data.items() if key not in  ["userID", "password"]}
        ##
        # print("paso 2 extrafields", extra_fields)
        if not user_ID or not user_pswd:
            return Response(request=request, data={"data": "Ingrese un nombre de usuario o correo o numero de documento, campo obligatorio"}, status=status.HTTP_400_BAD_REQUEST)
        ##
        # print("paso 3", user_ID.strip(), len(user_ID))
        user_auth = authenticate(request, userID=  user_ID.strip(), password=user_pswd.strip(), **extra_fields)
        ##
        # print("paso 4")
        if user_auth!=None:
            # print("paso 5 user auth !=None")
            login(request, user_auth)
            user_ser= UserSerializer(user_auth).data
            # print(user_ser)
            return Response(request=request, data={"data": "Usuario logeado con exito", "user": UserSerializer(user_auth).data}, status=status.HTTP_200_OK)
        return Response(request=request, data={"data": "Error en el login", "DATOS":{"user_auth": user_auth, "user_ID":user_ID, "user_pswd":user_pswd, "extra_fields":extra_fields}}, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        try:
            logout(request)
            return Response(request=request, status=status.HTTP_200_OK)
        except:
            return Response(request=request, data={"data":"Algo salió mal con el cierre de sesión"},status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request, username):
        if not username: 
            return Response(request=request, data={"details": "Ingrese un nombre de usuario"}, status=status.HTTP_400_BAD_REQUEST)
        if not get_user_model().objects.filter(username=username).exists():
            return Response(request=request, data={"details": "Este usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)
        user_model = get_user_model().objects.get(username=username)

        if not user_model:
            return Response(request=request, data={"data": "Usuario no encontrado", "user":user_model}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # print('si existe', user_model.toDict())
            user= UNPetUserManager(user_instance=user_model)
            # print('por user_instance se pudo', user_model.toDict())
            # userB= UNPetUserManager(user_id=user_model.id)
            # print('por id se pudo', user_model.toDict())
            # print(userA, userB)
            return Response(request=request, data={"data": "Usuario encontrado", "user": user.toDict()}, status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        # Verifica si el usuario ha iniciado sesión
        user = UNPetUserManager(user_instance=request.user)
        return Response(request=request, data={'data': 'datos del perfil', 'profile': user.toDict()}, status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request):
        current_user = ProfileSerializer(instance=request.user,data= request.data,partial=True)
        # print('USUARIO PROFILE PUT:', request.data, '====\n')
            # Valida y actualiza los campos de la instancia
        if current_user.is_valid():
            current_user.save()
            return Response(request=request, data={'data': 'Datos del usuario actualizados con exito','oldUserData':ProfileSerializer(request.user).data, 'newUserData':current_user.data}, status=status.HTTP_200_OK)
        else:
            return Response(request=request, data={'data': 'Error al actualizar los datos del usuario'}.update(current_user.errors), status=status.HTTP_400_BAD_REQUEST)
        



        
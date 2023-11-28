from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from .serializer import UserSerializer, ProfileSerializer, OrganizacionSerializer
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework import permissions,status
from rest_framework.response import Response
from utils.unpet_user import UNPetUserManager
from utils.firebase_manager import uploadUserIMG
from .models import Organizacion, Persona
import os
from django.http import JsonResponse

debug=True

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


class PasswordResetRequestView(APIView):

    def post(self, request):
        try:
            email = request.data.get('email')
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # send email with uid and token
            mail_subject = 'Restablecer su contraseña'
            domain = 'unpet-web.onrender.com'  # replace with your domain
            reset_link = f'http://{domain}/password-reset-confirm/{uid}/{token}/'
            message = f'Hola {user.username},\n\nHas solicitado restablecer tu contraseña. Por favor, ve a la siguiente página y elige una nueva contraseña:\n\n{reset_link}\n\nSi no has solicitado esto, por favor, ignora este correo electrónico.\n\n¡Gracias!'

            send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST) # email does not exist
        
class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                # reset password
                new_password = request.data.get('new_password')
                user.set_password(new_password)
                user.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST) # invalid link

class ChangePasswordView(APIView):
    def post(self, request):
        try:
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')
            if new_password != confirm_password:
                return Response({"error": "Las contraseñas no coinciden"}, status=status.HTTP_400_BAD_REQUEST)
            user = request.user
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse

class get_csrf(APIView):

    def get(self, request):
        csrf_token = get_token(request)
        return Response({'csrfToken': csrf_token})

        
class SessionView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        isAuthenticated = request.user.is_authenticated
        username = None
        urlfoto = None
        userType = 'Anonymous'

        if isAuthenticated:
            U = UNPetUserManager(user_id=request.user.id)
            username = request.user.username
            urlfoto = U.get_role_instance.urlfoto
            userType= U.get_role_instance.__class__.__name__

        return JsonResponse(data={'isAuthenticated': isAuthenticated, 'username': username, 'urlfoto': urlfoto, 'userType': userType})

class AdminRegister(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        pass

class front_test(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        return Response(data={"data": "test ok"}, status= status.HTTP_200_OK)
    def post(self, request):
        request.user
        return Response(data={"data": "test ok"}, status= status.HTTP_200_OK)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        users = [u.username for u in get_user_model().objects.all()]
        orgs = [u.username for u in Organizacion.objects.all()]
        personas = [u.username for u in Persona.objects.all()]
        return Response(data={"Usuarios registrados": users, "Organizaciones registradas": orgs, "Personas registradas": personas})
    def post(self, request):
        
        user_email = request.data.get('email')
        username = request.data.get('username')
        user_pswd = request.data.get('password')

        if 'terms' in request.data:
            del request.data['terms']

        for r in request.data:
            if debug:print(r, type(r))
        if debug:print(dict(request.data))
        photo = request.FILES.get('photo_file')

        photo2 = request.data.get('photo_file')
        
        if debug:print('LA FOTO ESTÁ AQUI:-->', type(photo), photo, type(photo2), photo2)
        photo = request.data.get('photo_file') if photo is None else photo
        # if 'image' not in photo.content_type.lower():
        #     resp={"error":"El archivo que envió no es de tipo imagen"}
        #     return Response(data=resp, status= status.HTTP_400_BAD_REQUEST)

        


        extra_fields = {key: value for key, value in request.data.items() if key not in  ['email', 'username', 'password']}
        user_model = get_user_model()
        ##
        if not username.strip():
            resp={"error":"Ingrese un username, campo obligatorio"}
            print('username falta')
            return Response(data=resp, status= status.HTTP_400_BAD_REQUEST)
        ##

        if user_model.objects.filter(email=user_email).exists():
            user_same_email= get_user_model().objects.get(email=user_email)
            print('El usuario con ese correo ya existe, es el siguiente.', UserSerializer(user_same_email).data, 'datos actuales: ', user_email, username, user_pswd)
            return Response(data={"data": "El usuario con ese correo ya existe, es el siguiente...", "user": UserSerializer(user_same_email).data}, status= status.HTTP_400_BAD_REQUEST)
        ##
        if user_model.objects.filter(username=username).exists():
            user_same_username= get_user_model().objects.get(username=username)
            print('El usuario con ese username ya existe, es el siguiente:', UserSerializer(user_same_username).data)

            return Response(data={"data": "El usuario con ese nombre de usuario ya existe, es el siguiente...", "user": UserSerializer(user_same_username).data}, status= status.HTTP_400_BAD_REQUEST)

        user_obj, rol_obj = user_model.objects.create_Persona(email=user_email,username= username, password=user_pswd, **extra_fields)
        # list_u = [ (u, u.id, u.username, u.password) for u in get_user_model().objects.all()]
        # for u in list_u:
        #     if debug:print('usuario-->',u)
        print('autenticando: ', user_obj.username, username, user_pswd)
        user_auth = authenticate(request, userID=username, password=user_pswd)
        ##
        if user_auth:
            login(request, user_auth)
            if photo is not None:
                linkIMG=uploadUserIMG(foto=photo, nombre=f'user-img-{user_auth.id}')
                if debug:print('IMAGEN SUBIDA, EL LINK ES: \n\n\n', linkIMG, '\n\n\n')
                if debug:print('objetos:...>', user_obj, type(user_obj), rol_obj, type(rol_obj))
                if debug:print('\n\nmas datos de objetos: ', user_auth, type(user_auth), user_obj, type(user_obj), rol_obj, type(rol_obj), 'id de user_obj: ', user_obj.id, 'id de rol_obj: ', rol_obj.id, user_obj.username, rol_obj.username)
                try:
                    user= UNPetUserManager(user_instance=user_obj, role_instance=rol_obj)
                    user.role_instance.urlfoto=linkIMG
                    user.save()
                except Exception as e:
                    if debug:print('error en el login xy: ', e)
                return Response(data={"data": "Usuario registrado con exito", "user": UserSerializer(user_obj).data, "login":True}, status=status.HTTP_201_CREATED)
        if debug:print('user_auth es None: ', user_auth, type(user_auth), user_obj, type(user_obj), rol_obj, type(rol_obj), 'id de user_obj: ', user_obj.id, 'id de rol_obj: ', rol_obj.id, user_obj.username, rol_obj.username)
        list_u = [ (u, u.id, u.username, u.password) for u in get_user_model().objects.all()]
        # for u in list_u:
        #     if debug:print(u)
        # list_p = [ (p, p.id, p.username) for p in Persona.objects.all()]
        # for p in list_p:
        #     if debug:print(p)

        print('ERROR FINAL: NO SE PUDO HACER NADA:',    user_obj, type(user_obj), rol_obj, type(rol_obj), 'id de user_obj: ', user_obj.id, 'id de rol_obj: ', rol_obj.id, user_obj.username, rol_obj.username)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class OrganizationRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        org_email = request.data.get('email')
        orgname = request.data.get('username')
        org_pswd = request.data.get('password')
        org_nit = request.data.get('nit')
        photo = request.FILES.get('photo_file')

        photo2 = request.data.get('photo_file')
        if 'terms' in request.data:
            del request.data['terms']
        if debug:print('LA FOTO ESTÁ AQUI:-->', type(photo), photo, type(photo2), photo2)
        photo = request.data.get('photo_file') if photo is None else photo

        # if 'image' not in photo.content_type.lower():
        #     return Response(data={"data": "El archivo que envió no es de tipo imagen"}, status= status.HTTP_400_BAD_REQUEST)
        
        extra_fields = {key: value for key, value in request.data.items() if key not in  ['email', 'username', 'password']}
        user_model = get_user_model()
        ##

        if not orgname.strip():
            return Response(data={"data": "Ingrese un nombre de organizacion, campo obligatorio"}, status= status.HTTP_400_BAD_REQUEST)
    
        if not org_nit.strip():
            return Response(data={"data": "Ingrese un NIT , campo obligatorio"}, status= status.HTTP_400_BAD_REQUEST)

        ##
        if user_model.objects.filter(email=org_email).exists():
            user_obj= get_user_model().objects.get(email=org_email)
            return Response(data={"data": "El usuario ya existe, es el siguiente...", "user": UserSerializer(user_obj).data}, status= status.HTTP_400_BAD_REQUEST)
        ##
        user_obj, rol_obj = user_model.objects.create_Organization(email=org_email,username= orgname, password=org_pswd, **extra_fields)
        user_auth = authenticate(request, userID=user_obj.username, password=org_pswd, **extra_fields)
        ##
        if user_auth:
            login(request, user_auth)
            linkIMG=uploadUserIMG(foto=photo, nombre=f'user-img-{user_auth.id}')
            user= UNPetUserManager(user_instance=user_obj, role_instance=rol_obj)
            user.role_instance.urlfoto=linkIMG
            user.save()
            if debug:print('organizacion creada!, link de la img: ', linkIMG)
            return Response(data={"data": "Organizacion registrada con exito", "user": UserSerializer(user_obj).data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = (SessionAuthentication,)
#     if debug:print('login paso 0')
#     def post(self, request):
        
#         if 'HTTP_ORIGIN' in request.META:
#             # Obtener el valor del encabezado 'Origin'
#             origin = request.META['HTTP_ORIGIN']
#             # Imprimir el host del frontend
#             if debug:print(f"Host del frontend: {origin}")
#         else:
#             # No se proporcionó el encabezado 'Origin' en la solicitud
#             if debug:print("No se proporcionó el encabezado 'Origin' en la solicitud")
#         if debug:print('login paso 0 post')

#         if request.user.is_authenticated:
#             if debug:print('login paso 0 post está authenticado')
#             resp={"error":"Usuario ya registrado"}
#             return Response(data=resp, status=status.HTTP_400_BAD_REQUEST)
#         # if debug:print("paso 0", request.data.get("userID"))
#         user_ID = request.data.get("userID")
#         user_pswd = request.data.get("password")
#         if debug:print('login paso 1 recojiendo datos:', user_ID, user_pswd)
#         # if debug:print("paso 1")
#         extra_fields = {key: value for key, value in request.data.items() if key not in  ["userID", "password"]}
#         if debug:print('login paso 2 extrafields:', extra_fields)
#         ##
#         # if debug:print("paso 2 extrafields", extra_fields)
#         if not user_ID or not user_pswd:
#             if debug:print('login paso 2 userId y password no tienen nada ')
#             resp={"error":"Ingrese un nombre de usuario o correo o numero de documento, campo obligatorio"}
#             return Response(data=resp, status=status.HTTP_400_BAD_REQUEST)
#         ##
#         # if debug:print("paso 3", user_ID.strip(), len(user_ID))
#         if debug:print('login paso 3 authenticando')
#         user_auth = authenticate(request, username=  user_ID.strip(), password=user_pswd.strip(), **extra_fields)
#         if debug:print('login paso 3 authenticando', user_auth, type(user_auth))
#         ##
#         # if debug:print("paso 4")
#         if user_auth is not None and user_auth.is_authenticated:
#             if debug:print('login paso 4 user_auth no es None, autenticado!, is_authenticated?-->\n-->',user_auth, user_auth.is_authenticated )
#             login(request, user_auth)
#             sessionid = request.session.session_key
#             if debug:print('esta es la sessionid--> ', sessionid)
#             user_ser = UserSerializer(user_auth).data
#             resp = {"ok": "Usuario logeado con exito", "user": user_ser, "sessionid": sessionid}
#             return Response(data=resp, status=status.HTTP_200_OK)
#         else:
#             if debug:print('login error en el login', request, request.data, request.user)
#             resp = {"error": "Usuario y contraseña incorrectos"}
#             return Response(data=resp, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        userID = request.data.get('userID')
        password = request.data.get('password')

        if userID is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = get_user(userID)

        if user is None:
            return Response({'error': 'Usuario no encontrado'},
                            status=status.HTTP_404_NOT_FOUND)

        user = authenticate(userID=userID, password=password)

        if user is not None:
            login(request, user)
            # Login successful, return user detail
            return Response(data={"msg":"login con exito!", "user":{**user.toDict()}})
        else:
            return Response({'error': 'Credenciales inválidas'},
                            status=status.HTTP_400_BAD_REQUEST)


# class UserLogout(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = ()
#     def post(self, request):
#         if debug:print('logout paso 0 ', request)
#         try:
#             if debug:print('logout paso 1 ')
#             logout(request)
#             if debug:print('logout paso 2 ')
#             return Response(status=status.HTTP_200_OK)
#         except Exception as e:
#             if debug:print('logout paso 2 except e:', e)
#             return Response(data={"data":"Algo salió mal con el cierre de sesión"},status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'detail': 'You\'re not logged in.'}, status=400)

        logout(request)
        return Response({'detail': 'Successfully logged out.'})
    

class UserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request, username):
        if not username: 
            return Response(data={"detail": "Ingrese un nombre de usuario"}, status=status.HTTP_400_BAD_REQUEST)
        if not get_user_model().objects.filter(username=username).exists():
            return Response(data={"detail": "Este usuario no existe", "userFound":False}, status=status.HTTP_400_BAD_REQUEST)
        user_model = get_user_model().objects.get(username=username)

        # if debug:print('si existe', user_model.toDict())
        user= UNPetUserManager(user_instance=user_model)
        # if debug:print('por user_instance se pudo', user_model.toDict())
        # userB= UNPetUserManager(user_id=user_model.id)
        # if debug:print('por id se pudo', user_model.toDict())
        # if debug:print(userA, userB)
        if request.user.is_authenticated:
            role_obj = user.get_role_instance
            data = user.toDict()
            data['telefono'] = role_obj.telefono
            return Response(data={"detail": "Usuario encontrado", "user": data}, status=status.HTTP_200_OK)

        return Response(data={"detail": "Usuario encontrado", "user": user.toDict()}, status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        # Verifica si el usuario ha iniciado sesión
        user = UNPetUserManager(user_instance=request.user)
        return Response(data={'user': user.toDict()}, status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request):
        current_user = ProfileSerializer(instance=request.user,data= request.data,partial=True)
        # if debug:print('USUARIO PROFILE PUT:', request.data, '====\n')
            # Valida y actualiza los campos de la instancia
        if current_user.is_valid():
            current_user.save()
            return Response(data={'detail':'Encontrado','oldUserData':ProfileSerializer(request.user).data, 'newUserData':current_user.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail':'No encontrado',}.update(current_user.errors), status=status.HTTP_400_BAD_REQUEST)
    



import os
from django.http import HttpResponse

class getHTML(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def get(self, request, filename):
        if not filename:
            return HttpResponse('Filename not provided', status=status.HTTP_400_BAD_REQUEST)
        route = '../public/texts'
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),route, filename)
        if debug:print(file_path)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                contents = f.read()
                #print('archivo html:  ', contents, type(contents))
                return HttpResponse( content=contents,content_type='text/html')
        except FileNotFoundError:
            return Response(f'File {filename} not found', status=status.HTTP_404_NOT_FOUND)


def get_user(userID):
        # Comprobar si userID es una dirección de correo electrónico
        user= get_user_model()
        import re
        patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron_correo, userID):
            # Intentar obtener el usuario por correo electrónico
            try:
                U = user.objects.get(email=userID)
            except user.DoesNotExist:
                return None
        else:
            try:
                U = user.objects.get(username=userID)
            except user.DoesNotExist:
                return None
        return U



# from django.core.mail import send_mail
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.sites.shortcuts import get_current_site

# class PasswordResetView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             user = None

#         if user is not None:
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             current_site = get_current_site(request)
#             mail_subject = 'Recuperación de contraseña'
#             message = 'Por favor, ve al siguiente enlace para restablecer tu contraseña: http://{}/reset/{}/{}/'.format(current_site.domain, uid, token)

#             send_mail(
#                 mail_subject,
#                 message,
#                 'from@example.com',
#                 [email],
#                 fail_silently=False,
#             )
        
#         return Response({"message": "Email sent"}, status=status.HTTP_200_OK)
    

# class PasswordResetConfirmView(APIView):
#     def post(self, request, uidb64, token):
#         UserModel = get_user_model()
#         try:
#             uid = urlsafe_base64_decode(uidb64).decode()
#             user = UserModel._default_manager.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
#             user = None

#         if user is not None and default_token_generator.check_token(user, token):
#             # Aquí puedes implementar la lógica para permitir al usuario restablecer su contraseña.
#             # Por ahora, solo devolveré un mensaje de éxito.
#             return Response({"message": "Password reset link is valid"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid link"}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from accounts.serializer import UserSerializer, ProfileSerializer, OrganizationSerializer
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import permissions,status
from utils.json_respond import Response
from utils.unpet_user import UNPetUserManager
from accounts.models import Organizacion, Persona


class CreatePost(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        return Response(request=request,data={"Usuarios registrados":{u.username for u in get_user_model().objects.all()},
                                                 "Organizaciones registradas":{u.username for u in Organizacion.objects.all()},
                                                 "Personas registradas":{u.username for u in Persona.objects.all()}})
    def post(self, request):
        pass

class EditPost(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        return Response(request=request,data={"Usuarios registrados":{u.username for u in get_user_model().objects.all()},
                                                 "Organizaciones registradas":{u.username for u in Organizacion.objects.all()},
                                                 "Personas registradas":{u.username for u in Persona.objects.all()}})
    def post(self, request):
        pass

class DeletePost(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        return Response(request=request,data={"Usuarios registrados":{u.username for u in get_user_model().objects.all()},
                                                 "Organizaciones registradas":{u.username for u in Organizacion.objects.all()},
                                                 "Personas registradas":{u.username for u in Persona.objects.all()}})
    def post(self, request):
        pass



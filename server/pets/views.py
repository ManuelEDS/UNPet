from rest_framework import viewsets
from .serializer import MascotaSerializer
from .models import Mascota
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
# Create your views here.
from rest_framework import generics, permissions
from .serializer import MascotaSerializer, MascotaUpdateSerializer
from rest_framework.exceptions import ValidationError

from rest_framework.exceptions import ValidationError

class MascotaListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("No se han enviado las credenciales., is authenticated: ",request.user.is_authenticated)
            print("Token de sesión:", request.session.get("SESSION_KEY"))

        else:
            print("se han enviado las credenciales. SII")
            print("Token de sesión:", request.session.get("SESSION_KEY"))
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        if user.groups.filter(name='Organizacion').exists():
            serializer.save(idorganizacion=user.organizacion)
        else:
            raise ValidationError("No tienes permisos para crear esta mascota.")



class MascotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    queryset = Mascota.objects.all()
    serializer_class = MascotaUpdateSerializer
  # Requiere autenticación

class MascotasOrganizacionListView(generics.ListAPIView):
    serializer_class = MascotaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,) 
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='Organizacion').exists():
            return Mascota.objects.filter(idorganizacion=user.id)
        else:
            return Mascota.objects.none()
    

    # class PetsView(viewsets.ModelViewSet): # NOTA: CREAR MASCOTA EXLUSIVO DE CREAR PUBLICACION?
#     # Una organizacion puede crear mascota para en otro lugar subir una publicacion? o todo en uno?
#     # lo de que si es exclusivo es que todas estas cosas son de Organizacion, no personas
#     # permission_classes = (permissions.IsAuthenticated,)
#     # authentication_classes = (SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#     authentication_classes = (SessionAuthentication,)
#     serializer_class = MascotaSerializer
#     queryset = Mascota.objects.all()
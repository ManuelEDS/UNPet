from .models import Mascota
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics, permissions
from .serializer import MascotaSerializer, MascotaUpdateSerializer
from rest_framework.exceptions import ValidationError

class MascotaListCreateView(generics.ListCreateAPIView):
    """Para crear una mascota"""
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.groups.filter(name='Organizacion').exists():
            serializer.save(idorganizacion=user.organizacion)
        else:
            raise ValidationError("No tienes permisos para crear esta mascota.")

class MascotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Para obtener, editar y eliminar una mascota por su id"""
    queryset = Mascota.objects.all()
    serializer_class = MascotaUpdateSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if request.user.id != obj.idorganizacion.id:
                self.permission_denied(request)

class MascotasOrganizacionListView(generics.ListAPIView):
    """Permite listar todas las mascotas que pertenecen a la organización del usuario actual"""
    serializer_class = MascotaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,) 
    def get_queryset(self):
        user = self.request.user
        print('mascotas list org: ', user.id, user.groups.filter(name='Organizacion').exists(), user.is_authenticated)
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
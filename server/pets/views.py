from rest_framework import viewsets
from .serializer import MascotaSerializer
from .models import Mascota
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions,status
# Create your views here.


class PetsView(viewsets.ModelViewSet): # NOTA: CREAR MASCOTA EXLUSIVO DE CREAR PUBLICACION?
    # Una organizacion puede crear mascota para en otro lugar subir una publicacion? o todo en uno?
    # lo de que si es exclusivo es que todas estas cosas son de Organizacion, no personas
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()

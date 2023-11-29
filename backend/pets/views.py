from utils.firebase_manager import uploadUserIMG
from .models import Mascota
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics, permissions, status
from .serializer import MascotaSerializer, MascotaUpdateSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import Organizacion
from django.views.decorators.csrf import csrf_exempt

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
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def check_object_permissions(self, request, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE', 'POST']:
            pet = Mascota.objects.get(pk=obj.id)
            print('mascota retrieve: ', request.user.id, pet.idorganizacion)
            print('vamos a ver si es organizacion: ', request.user.groups.filter(name='Organizacion').exists())
            if request.user.id != pet.idorganizacion:
                self.permission_denied(request)

class MascotaUpdateView(APIView):
    """Para actualizar una mascota"""
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    @csrf_exempt
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        user = self.request.user
        if user.groups.filter(name='Organizacion').exists():
            pet = Mascota.objects.get(pk=pk)
            serializer = MascotaUpdateSerializer(pet, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ValidationError("No tienes permisos para editar esta mascota.")
        
class MascotaDeleteView(APIView):
    """Para eliminar una mascota"""
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def delete(self, request, pk, format=None):
        user = self.request.user
        if user.groups.filter(name='Organizacion').exists():
            pet = Mascota.objects.get(pk=pk)
            pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("No tienes permisos para eliminar esta mascota.")
        
class MascotaCreateView(APIView):
    """Para crear una mascota"""
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request, format=None):
        user = self.request.user
        if user.groups.filter(name='Organizacion').exists():
            data = request.data.copy()  # Hacer una copia de request.data
            photo = data.pop('photo_file', None)  # Extraer y eliminar 'photo_file' de data
            photo = request.FILES.get('photo_file') if photo is None else photo
            data.setdefault('adoptada', False)
            # Primero, crea la mascota sin la urlfoto
            serializer = MascotaSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                org = Organizacion.objects.get(pk=user.id)
                mascota = serializer.save(idorganizacion=org)

                # Luego, sube la imagen y obtén la URL
                if photo is not None:
                    
                    linkIMG = uploadUserIMG(foto=photo, nombre=f'user-img-{mascota.id}')
                    mascota.urlfoto = linkIMG
                    print('mascota urlfoto cuando hay foto: ', mascota.urlfoto, photo)
                else:
                    
                    mascota.urlfoto = "../../../public/default-post-img.jpg"
                    print('mascota urlfoto cuando no hay foto: ', mascota.urlfoto, photo)
                print('mascota urlfoto: ', mascota.urlfoto)

                # Finalmente, actualiza la mascota con la URL de la imagen
               
                mascota.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ValidationError("No tienes permisos para crear esta mascota.")

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
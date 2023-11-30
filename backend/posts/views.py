from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Publicacion, Comentario
from .serializer import PublicacionSerializer, ComentarioSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import  authentication
from django.contrib.auth import get_user_model
from accounts.models import Organizacion
from django.db import transaction
from pets.models import Mascota
from .models import Publicacion, Like
from django.http import Http404
import json


class LikePublicacion(APIView):
    def post(self, request, pk):
        publicacion = Publicacion.objects.get(pk=pk)
        like = Like.objects.create(
            user=request.user,
            content_object=publicacion
        )
        publicacion.likes += 1
        publicacion.save()
        return Response(status=status.HTTP_201_CREATED)


class LikedPublicaciones(APIView):
    def get(self, request):
        user = request.user
        liked_publicaciones = self.get_liked_publicaciones(user)
        serializer = PublicacionSerializer(liked_publicaciones, many=True)
        return Response(serializer.data)
    
    def get_liked_publicaciones(user):
        user_likes = Like.objects.filter(user=user)
        liked_publicaciones = [like.content_object for like in user_likes if isinstance(like.content_object, Publicacion)]
        return liked_publicaciones


class LikeComentario(APIView):
    def post(self, request, pk, comment_pk):
        comentario = Comentario.objects.get(pk=comment_pk)
        like = Like.objects.create(
            user=request.user,
            content_object=comentario
        )
        comentario.likes += 1
        comentario.save()
        return Response(status=status.HTTP_201_CREATED)
    

class LikedComentarios(APIView):
    def get(self, request):
        user = request.user
        liked_comentarios = self.get_liked_comentarios(user)
        serializer = ComentarioSerializer(liked_comentarios, many=True)
        return Response(serializer.data)
    
    def get_liked_comentarios(user):
        user_likes = Comentario.objects.filter(user=user)
        liked_publicaciones = [like.content_object for like in user_likes if isinstance(like.content_object, Publicacion)]
        return liked_publicaciones
    
def print_post_create(req):
    post_data = req.data.get('post', {})  # Obtener una lista de valores bajo la clave 'post'
    print('post_data print_post_create: ', post_data)
    if post_data:
        idorganizacion = post_data.get('idorganizacion')
        estado = post_data.get('estado')
        titulo = post_data.get('titulo')
        descripcion = post_data.get('descripcion')
        n_mascotas = post_data.get('n_mascotas')
        n_mascotas_adoptadas = post_data.get('n_mascotas_adoptadas')
        mascotas = post_data.get('mascotas', [])

        print(f'idorganizacion: {idorganizacion}')
        print(f'estado: {estado}')
        print(f'titulo: {titulo}')
        print(f'descripcion: {descripcion}')
        print(f'n_mascotas: {n_mascotas}')
        print(f'n_mascotas_adoptadas: {n_mascotas_adoptadas}')

        for mascota in mascotas:
            mascota_id = mascota.get('id')
            print(f'Mascota ID: {mascota_id}')
class PublicacionCreate(APIView): #CREAR PUBLICACION CON MASCOTAS 
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        post_data = json.loads(request.data['post'])
        mascotas = json.loads(post_data["mascotas"])
        mascotas = [json.loads(mascota) for mascota in mascotas]

        print('mascotas v1', mascotas)
        if 'mascotas' in post_data:
            del post_data['mascotas']

        post_data['n_mascotas'] = int(post_data['n_mascotas'])
        post_data['n_mascotas_adoptadas'] = int(post_data['n_mascotas_adoptadas'])
        post_data['idorganizacion'] = request.user.id
 
        
        userid= request.user.id
        org= post_data.get('idorganizacion')
        
        print('legada de datos','post_data: ', post_data, '\mascotas: ', mascotas,'userid', userid, 'org: ',org)
        if org is None:
            if Organizacion.objects.filter(id=userid).exists():
                post_data['idorganizacion']= userid
            else:
                return Response({'error': 'No existe organizacion con ese id'}, status=status.HTTP_400_BAD_REQUEST) 
        else:
            if org!=userid:
                return Response({'error': 'El usuario actual no coincide con la idorganizacion'}, status=status.HTTP_400_BAD_REQUEST)
        # mas codigo abajo        
        
        organizacion = Organizacion.objects.get(id=userid)
        post_data['idorganizacion'] = organizacion

        post1 = Publicacion.objects.create(**post_data)
        
        if post1:
            
            print("la publicacion se creo, se procede a vincular las mascotas las mascotas")
            for pet_data in mascotas:
                # Obtiene la mascota de la base de datos
                mascota = Mascota.objects.get(id=pet_data['id'])

                # Relaciona la mascota con la publicación
                mascota.publicacion = post1
                mascota.save()
            print('serializer.data', post1, post_data)
            print('mascotas vinculadas')
            return Response({"status":"creado!"}, status=status.HTTP_201_CREATED)

        return Response({"error":"No se pudo crear la publicacion"}, status=status.HTTP_400_BAD_REQUEST)


class PublicacionRecentList(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5  # Set page size to 5
        publicaciones = Publicacion.objects.all().order_by('-fechapublicacion')
        result_page = paginator.paginate_queryset(publicaciones, request)
        if result_page is not None:
            serializer = PublicacionSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
class PublicacionesOrg(APIView):
  def get(self, request, org_username):
        paginator = PageNumberPagination()
        paginator.page_size = 5  # Set page size to 5
        organizacion = get_object_or_404(Organizacion, username=org_username)
        publicaciones = Publicacion.objects.filter(idorganizacion=organizacion).order_by('-fechapublicacion')
        result_page = paginator.paginate_queryset(publicaciones, request)
        serializer = PublicacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

        
class PublicacionTrendList(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5  # Set page size to 5
        publicaciones = Publicacion.objects.all().order_by('-likes', '-fechapublicacion')
        result_page = paginator.paginate_queryset(publicaciones, request)
        if result_page is not None:
            serializer = PublicacionSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
    @authentication_classes([authentication.SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def post(self, request):
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicacionDetail(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        serializer = PublicacionSerializer(publicacion)
        return Response({"post":serializer.data})


class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
            """
            This view should return a list of all the comments
            for the post as determined by the post's PK.
            """
            pk = self.kwargs['pk']
            return Comentario.objects.filter(publicacion=pk)
    
class ComentarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Http404:
            return Response([])

    def get_queryset(self):
        """
        This view should return a list of all the comments
        for the post as determined by the post's PK.
        """
        pk = self.kwargs['pk']
        comment_pk = self.kwargs['comment_pk']
        data= Comentario.objects.filter(id=comment_pk, publicacion=pk)
        return [] if not data else data

class ComentarioRespuestasView(generics.ListAPIView):
    serializer_class = ComentarioSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if Comentario.objects.filter(pk=self.kwargs['pk']).exists():
            comentario = Comentario.objects.get(pk=self.kwargs['pk'])
            return comentario.respuestas.all()
        return Comentario.objects.none()
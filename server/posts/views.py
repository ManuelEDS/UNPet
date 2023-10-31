from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Publicacion, Comentario
from .serializer import PublicacionSerializer, ComentarioSerializer
from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework import  authentication

class PublicacionSearch(generics.ListAPIView):
    serializer_class = PublicacionSerializer
    pagination_class = PageNumberPagination()
    pagination_class.page_size = 5  # Set page size to 5
    def get_queryset(self):
        query = self.request.query_params.get('q')
        queryset = Publicacion.objects.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )
        return queryset
    
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
    def get(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        serializer = PublicacionSerializer(publicacion)
        return Response(serializer.data)


class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ComentarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ComentarioRespuestasView(generics.ListAPIView):
    serializer_class = ComentarioSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        comentario = Comentario.objects.get(pk=self.kwargs['pk'])
        return comentario.respuestas.all()
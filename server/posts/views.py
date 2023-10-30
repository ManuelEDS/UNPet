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

class PublicacionSearch(generics.ListAPIView):
    serializer_class = PublicacionSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        queryset = Publicacion.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        )
        return queryset


class PublicacionList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        paginator = PageNumberPagination()
        publicaciones = Publicacion.objects.all().order_by('-likes', '-created_at')
        result_page = paginator.paginate_queryset(publicaciones, request)
        serializer = PublicacionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicacionDetail(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        serializer = PublicacionSerializer(publicacion)
        return Response(serializer.data)

class ComentarioList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        publicacion = get_object_or_404(Publicacion, pk=pk)
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(publicacion=publicacion, autor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComentarioDetail(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk, comentario_pk):
        comentario = get_object_or_404(Comentario, pk=comentario_pk, publicacion=pk, autor=request.user)
        serializer = ComentarioSerializer(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, comentario_pk):
        comentario = get_object_or_404(Comentario, pk=comentario_pk, publicacion=pk, autor=request.user)
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
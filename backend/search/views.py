from rest_framework.response import Response
from posts.models import Publicacion
from posts.serializer import PublicacionSerializer
from accounts.serializer import UserSerializer, PersonaSerializer, OrganizacionSerializer
from accounts.models import Persona, Organizacion
from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
# Create your views here.


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5

class GeneralSearch(generics.ListAPIView):
    pagination_class = CustomPageNumberPagination
    serializer_class = PublicacionSerializer


    def get_queryset(self):
        response_data = {'results': []}
        query = self.request.query_params.get('q', '')
        if query.startswith('@'):
            username, _, query = query.lstrip('@').partition(' ')
            if get_user_model().objects.filter(username=username).exists():
                try:
                    org = Organizacion.objects.get(username=username)
                    org_serializer = OrganizacionSerializer(org)
                    response_data['results'].insert(0, org_serializer.data)
                    if query:
                        data= org.publicaciones_organizacion.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))
                        pub_serializer = PublicacionSerializer(data, many=True)
                        response_data['results'].extend(pub_serializer.data)
                        return response_data['results']
                    else:
                        data = org.publicaciones_organizacion.all()
                        pub_serializer = PublicacionSerializer(data, many=True)
                        response_data['results'].extend(pub_serializer.data)
                        return response_data['results']
                except Organizacion.DoesNotExist:
                    if query:
                        data = Publicacion.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query)) 
                        pub_serializer = PublicacionSerializer(data, many=True)
                        return pub_serializer.data
                    else:
                        return Publicacion.objects.none()
            else:
                data = Publicacion.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))
                pub_serializer = PublicacionSerializer(data, many=True)
                return pub_serializer.data
        else:
            data = Publicacion.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))
            pub_serializer = PublicacionSerializer(data, many=True)
            return pub_serializer.data
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None and len(page) > 0:
            return self.get_paginated_response(page)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'count': len(serializer.data),
            'next': None,
            'previous': None,
            'results': serializer.data
        }
        query = self.request.query_params.get('q', '')
        username, _, query = query.lstrip('@').partition(' ')
        if 'q' in self.request.query_params and self.request.query_params['q'].startswith('@'):
            query = self.request.query_params.get('q', '')
            username, _, query = query.lstrip('@').partition(' ')
            if get_user_model().objects.filter(username=username).exists():
                try:
                    persona = Persona.objects.get(username=username)
                    persona_serializer = PersonaSerializer(persona)
                    response_data['results'].insert(0, persona_serializer.data)
                except Persona.DoesNotExist:
                    try:
                        org = Organizacion.objects.get(username=username)
                        org_serializer = OrganizacionSerializer(org)
                        response_data['results'].insert(0, org_serializer.data)
                    except Organizacion.DoesNotExist:
                        pass
        print('linea de codigo final, response data:\n', response_data)
        return Response(response_data)




class PublicacionSearch(generics.ListAPIView):
    serializer_class = PublicacionSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('q')
        return Publicacion.objects.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'count': len(serializer.data),
            'next': None,
            'previous': None,
            'results': serializer.data
        }
        return Response(response_data)
    



class UserSearch(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', '').lstrip('@')
        exact_match = get_user_model().objects.filter(username__iexact=query)
        similar_match = get_user_model().objects.filter(username__icontains=query).exclude(username__iexact=query)
        return exact_match.union(similar_match)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'count': len(serializer.data),
            'next': None,
            'previous': None,
            'results': serializer.data
        }
        return Response(response_data)

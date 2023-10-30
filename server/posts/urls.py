from django.urls import path, include
from .views import PublicacionList, PublicacionDetail, ComentarioList, ComentarioDetail, PublicacionSearch

urlpatterns = [
    path('api/publicaciones/', PublicacionList.as_view(), name='publicacion-list'),
    path('api/publicaciones/<int:pk>/', PublicacionDetail.as_view(), name='publicacion-detail'),
    path('api/publicaciones/<int:pk>/comentarios/', ComentarioList.as_view(), name='comentario-list'),
    path('api/publicaciones/<int:pk>/comentarios/<int:comentario_pk>/', ComentarioDetail.as_view(), name='comentario-detail'),
    path('api/publicaciones/page/<int:page>/', PublicacionList.as_view(), name='publicacion-list-page'),
    path('api/publicaciones/search/', PublicacionSearch.as_view(), name='publicacion-search'),


]
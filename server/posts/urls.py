from django.urls import path, include
from .views import PublicacionList, PublicacionDetail, ComentarioList, ComentarioDetail, PublicacionSearch

urlpatterns = [
    path('api/posts/', PublicacionList.as_view(), name='publicacion-list'),
    path('api/posts/<int:pk>/', PublicacionDetail.as_view(), name='publicacion-detail'),
    path('api/posts/<int:pk>/comentarios/', ComentarioList.as_view(), name='comentario-list'),
    path('api/posts/<int:pk>/comentarios/<int:comentario_pk>/', ComentarioDetail.as_view(), name='comentario-detail'),
    path('api/posts/page/<int:page>/', PublicacionList.as_view(), name='publicacion-list-page'),
    path('api/posts/search/', PublicacionSearch.as_view(), name='publicacion-search'),


]
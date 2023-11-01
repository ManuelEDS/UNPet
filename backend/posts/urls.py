from django.urls import path
from .views import (
    PublicacionRecentList,
    PublicacionTrendList,
    PublicacionDetail,
    PublicacionSearch,
    ComentarioListCreateView,
    ComentarioDetailView,
    ComentarioRespuestasView,
)

urlpatterns = [
    path('api/posts/recent/', PublicacionRecentList.as_view(), name='publicacion-recent'),
    path('api/posts/trend/', PublicacionTrendList.as_view(), name='publicacion-trend'),
    path('api/posts/<int:pk>/', PublicacionDetail.as_view(), name='publicacion-detail'),
    path('api/posts/search/', PublicacionSearch.as_view(), name='publicacion-search'),
    path('api/posts/<int:pk>/comments/', ComentarioListCreateView.as_view(), name='comentario-list-create'),
    path('api/posts/<int:pk>/comments/<int:comment_pk>/', ComentarioDetailView.as_view(), name='comentario-detail'),
    path('api/posts/<int:pk>/comments/<int:comment_pk>/respuestas/', ComentarioRespuestasView.as_view(), name='comentario-respuestas'),
]

from django.urls import path
from .views import (
    PublicacionRecentList,
    PublicacionTrendList,
    PublicacionDetail,
    ComentarioListCreateView,
    ComentarioDetailView,
    ComentarioRespuestasView,
    PublicacionesOrg,
    LikePublicacion,
    LikeComentario,
    PublicacionCreate,
    PublicacionDelete,
)

urlpatterns = [
    path('api/posts/recent/', PublicacionRecentList.as_view(), name='publicacion-recent'),
    path('api/posts/trend/', PublicacionTrendList.as_view(), name='publicacion-trend'),
    path('api/posts/<int:pk>/', PublicacionDetail.as_view(), name='publicacion-detail'),
    path('api/posts/<int:pk>/delete/', PublicacionDelete.as_view(), name='publicacion-delete'),
    path('api/posts/<int:pk>/comments/', ComentarioListCreateView.as_view(), name='comentario-list-create'),
    path('api/posts/<int:pk>/comments/<int:comment_pk>/', ComentarioDetailView.as_view(), name='comentario-detail'),
    path('api/posts/<int:pk>/comments/<int:comment_pk>/answers/', ComentarioRespuestasView.as_view(), name='comentario-respuestas'),
    path('api/posts/<str:org_username>/posts/', PublicacionesOrg.as_view(), name='publicaciones_org'),
    path('api/posts/<int:pk>/like/', LikePublicacion.as_view(), name='publicacion-like'),
    path('api/posts/<int:pk>/comments/<int:comment_pk>/like/', LikeComentario.as_view(), name='comentario-like'),
    path('api/posts/create/', PublicacionCreate.as_view(), name='publicacion-create'),
]


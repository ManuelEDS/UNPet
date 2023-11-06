from django.urls import path
from .views import (
    GeneralSearch,
    PublicacionSearch,
    UserSearch,
)

urlpatterns = [
    path('api/general/', GeneralSearch.as_view(), name='general-search'),
    path('api/posts/', PublicacionSearch.as_view(), name='publicacion-search'),
    path('api/users/', UserSearch.as_view(), name='user-search'),
]









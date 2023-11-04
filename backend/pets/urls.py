from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# Add your custom routes here if needed

urlpatterns = [
    path('', include(router.urls)),
    path('api/pets/', views.MascotaListCreateView.as_view(), name='mascota-list-create'),
    path('api/pets/<int:pk>/', views.MascotaRetrieveUpdateDestroyView.as_view(), name='mascota-retrieve-update-destroy'),
    path('api/pets/organization/', views.MascotasOrganizacionListView.as_view(), name='mascotas-organizacion-list'),
    
]

# Other routes of your application


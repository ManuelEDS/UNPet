from rest_framework import viewsets
from .serializer import PetsSerializer
from .models import Pets

# Create your views here.


class PetsView(viewsets.ModelViewSet):
    serializer_class = PetsSerializer
    queryset = Pets.objects.all()

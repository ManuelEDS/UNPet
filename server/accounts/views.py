from django.contrib.auth import authenticate, login, logout
from . import re
from .models import User
from rest_framework import generics
from .serializer import UserSerializer

class PersonaList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def login_view(request):
    if request.method == 'POST':
        userID = request.POST['userID']
        password = request.POST['password']
        patron_correo= r'^[\w\.-]+@[\w\.-]+\.\w+$'
        user=None
        if re.match(patron_correo, userID):
            user = User.authenticate_by_email(request, email=userID, password=password)
        elif userID.isDigit():
            user = User.get_user_by_id(int(userID))
        else:
            user = authenticate(request, username=userID, password=password)


        if user is None:
            login(request, user)
            # Redirigir a una página después del inicio de sesión
            return redirect('dashboard')
        else:
            # Mostrar un mensaje de error
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

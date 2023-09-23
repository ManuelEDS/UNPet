
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
def home(request):
	return render(request, 'general/home.html')

@api_view(['POST'])
def user_register(request):
    user_email = request.POST['email']
    username = request.POST['username']
    user_pswd = request.POST['password']
    extra_fields = {key: value for key, value in request.POST.items() if key not in  ['email', 'username', 'password']}
    user_model = get_user_model()
    ##
    if not username.strip():
        messages.error(request, 'Algo salió mal con el nombre de usuario.')
        return render(request, 'app_users/signup.html')
    ##
    if user_model.objects.filter(email=user_email).exists():
        messages.error(request, 'Ya existe un usuario co este correo')
        return render(request, 'app_users/signup.html')
    ##
    user_obj = user_model.objects.create_user(email=user_email,username= username, password=user_pswd, **extra_fields)
    user_obj.save()
    user_auth = authenticate(userID=user_email, password=user_pswd, **extra_fields)
    ##
    if user_auth:
        login(request, user_auth)
        return Response({"details": "Usuario registrado con exito", "user": UserSerializer(user_obj).data})



def user_login(request):

    if request.method == 'POST':
            user_ID = request.POST['userID']
            user_pswd = request.POST['password']
            extra_fields = {key: value for key, value in request.POST.items() if key not in  ['email', 'username', 'password']}
            user_model = get_user_model()
            ##
            if not user_ID.strip() or not user_pswd.strip():
                messages.error(request, 'Ingrese correctamente sus datos de usuario')
                return render(request, 'app_users/login.html')
            ##
            user_auth = authenticate(userID= user_ID, password=user_pswd, **extra_fields)
            ##
            if user_auth:
                login(request, user_auth)
                return redirect('home')
    return render(request, 'app_users/login.html')

@login_required
def user_logout(request):
	try:
		logout(request)
	except:
		messages.error(request, 'Something is wrong.')
	return redirect('login')



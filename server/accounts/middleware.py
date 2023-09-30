# middleware.py
from django.contrib.auth.models import AnonymousUser

class UserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Agrega información del usuario al contexto
        user_info = {
            'userType': 'Anonymus',  # Valor predeterminado para usuarios anónimos
        }

        if request.user.is_authenticated:
                user_info['username'] = request.user.username
                user_info['userType'] = request.user.get_groups()


        request.user_info = user_info

        response = self.get_response(request)
        return response

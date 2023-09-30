
from rest_framework.response import Response as respuesta




def Response(request=None, data=None, status=200):
    print('\n\n\n\n\n',data, '\n\n\n\n\n',request,'\n\n\n\n\n', request.user, '\n\n', request.user_info)
    if request is None:
        data["user"] = {"userType": "Anonymus", "userObject":request.user}
    else:
        pass
    
    
    return respuesta(data=data, status=status)


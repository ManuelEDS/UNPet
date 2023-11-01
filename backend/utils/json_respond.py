
from rest_framework.response import Response as respuesta



def Response(request=None, data=None, status=200):
    #print('\n\n\n\n\n',data, '\n\n\n\n\n',request,'\n\n\n\n\n', request, '\n\n', request.user_info)
    keys= data.keys()
    if request is None:
        data["user"] = {"userType": "AnonymousUser"}
        return respuesta(data=data, status=status)
    else:
        if request.user.is_authenticated:
            if data.get('profile') is not None:
                pass
            elif 'userFound' in keys:
                #if data['userFound']==False:
                pass
            else:
                data['user']= request.user.toDict()
            return respuesta(data=data, status=status)
    return respuesta(data=data, status=status)


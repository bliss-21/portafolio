from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.
#parte del WS
from rest_framework import viewsets
from .serializer import UserSerializer
from rest_framework.response import Response#para el post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view

def validar_admin(username=None,password=None):
    usuario = User.objects.get(username=username,groups__name='ADMINISTRADOR')
    resp = usuario.check_password(password)
    return resp


class UserViewSet(viewsets.ModelViewSet):
    #creo que podemos modificarlo aqui
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def validar_administrador(request):
    "verifica las credenciales de un usuario administrador"
    try:
        username = request.query_params['username']
        password = request.query_params['password']
        usuario = User.objects.get(username=username,groups__name='ADMINISTRADOR')
        resp = usuario.check_password(password)
    except:
        return Response({"response": False, "message": "invalid parameters"})

    if resp:
        return Response({"respuesta": True, "username": usuario.username})
    else:
        return Response({"respuesta": False})
    


@api_view(['POST'])
def add_user(request):
    try:
        username = request.query_params['username_admin']
        password = request.query_params['password_admin']
        is_valido = validar_admin(username,password)
        print(is_valido)
        if is_valido:
            #creacion de usuario
            user = User()
            user.username = request.query_params['username']
            user.email = request.query_params['email']
            user.first_name = request.query_params['first_name']
            user.last_name = request.query_params['last_name']
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.date_joined = datetime.now()
            user.set_password(request.query_params['password'])
            user.save()
            #añadimos el usuario al el rol espesifico
            group_id = request.query_params['group_id']
            group = Group.objects.get(id = group_id)
            user.groups.add(group)
            return Response({"response": True, "message": "user create"})

        else:
            #Contraseñas incorrecta
            return Response({"response": False, "message": "not allowed"})

    except:
        #error en algun parametro
        return Response({"response": False, "message": "No user created"})


@api_view(['GET', 'POST'])
def hello_world(request):

    if request.method == 'POST':
        test_data_var = request.query_params['testData']
        return Response({"message": "Got some data!", "data": test_data_var})
    return Response({"message": "Hello, world!"})


#prueba 
@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def usuario_list(request):
    if request.method == 'GET':
        #tutorials = Tutorial.objects.all()
        usuarios = User.objects.all()

        #title = request.query_params.get('title', None)
        """username = request.query_params.get('username', None)"""

        #if title is not None:
        """if username is not None:
            #tutorials = tutorials.filter(title__icontains=title)
            usuarios = usuarios.filter(username__icontains=username)"""
        
        #tutorials_serializer = TutorialSerializer(tutorials, many=True)
        usuarios_serializer = UserSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':

        #tutorial_data = JSONParser().parse(request)
        print('asdasdasdasdasd',request.data)
        usuarios_data = JSONParser().parse(request.data)
        
        #tutorial_serializer = TutorialSerializer(data=tutorial_data)
        usuarios_serializer = UserSerializer(data=usuarios_data)
        print(request.data)
        #if tutorial_serializer.is_valid():
        if usuarios_serializer.is_valid():
            #tutorial_serializer.save()
            
            usuarios_serializer.save()
            
            #return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(usuarios_serializer.data, status=status.HTTP_201_CREATED)  

        #return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(usuarios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #elif request.method == 'DELETE':
        #count = Tutorial.objects.all().delete()
        #return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
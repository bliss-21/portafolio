from django.urls import path
from django.contrib.auth.urls import views as auth_views
from .views import *
from django.conf import settings


from rest_framework import routers
from .views import UserViewSet
from django.conf.urls import url 

router =  routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('hello_world', hello_world, name="hello_world"),
    path('validar_administrador', validar_administrador, name="validar_administrador"),
    path('add_user',add_user,name='add_user'),
    path('usuario', usuario_list,name='usuario'),
] + router.urls

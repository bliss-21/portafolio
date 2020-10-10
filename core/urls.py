from django.urls import path
from django.contrib.auth.urls import views as auth_views
from .views import *
from django.conf import settings

########__WS__##########
#from rest_framework import routers
#from .viewsets import AuthUserViewSet,UserViewSet

#router =  routers.SimpleRouter()
#router.register('api_login', AuthUserViewSet)
#router.register('api_login2', UserViewSet)

########################
urlpatterns = [

    #globales
    path('formulario_afiliacion',formulario_afiliacion, name="formulario_afiliacion"),

    #home's
    path('', home, name="home"),
    path('administrador', home_administrador, name="administrador"),
    path('cli_ex', home_cliente_externo, name="cli_ex"),
    path('cli_in', home_cliente_iterno, name="cli_in"),
    path('transport', home_trnasportista, name="transport"),
    path('consul', home_consultor, name="consul"),
    path('productor', home_productor, name="productor"),
    #redirigir
    path('redirigir',ValidarUsuario , name="redirigir"),

    #login
    path('ingreso_usuario/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    # PRODUCTOR
    path('producto_agregar',productor_agregar , name="productor_agregar"),
    path('productor_actualizar/<id_producto>/',productor_actualizar , name="productor_actualizar"),
    path('producto_eliminar/<id_producto>/',producto_eliminar , name="producto_eliminar"),

    #WS
    #path('prueba_login_found',prueba_login_found,name='prueba_login_found'),
] #+ router.urls
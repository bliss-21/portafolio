from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

#para los cursores
from django.db import connection

from .models import Calidad, Fruta, Producto, AuthUser, TipoAfiliacion, SolicitudAfilacion

#prueba:
from django.contrib.auth.decorators import user_passes_test

def is_administrador(user):
    return user.groups.filter(name='ADMINISTRADOR').exists()

def is_cli_ex(user):
    return user.groups.filter(name='CLIENTE_EXTERNO').exists()

def is_cli_in(user):
    return user.groups.filter(name='CLIENTE_INTERNO').exists()

def is_trasnp(user):
    return user.groups.filter(name='TRANSPORTISTA').exists()

def is_consul(user):
    return user.groups.filter(name='CONSULTOR').exists()

def is_productor(user):
    return user.groups.filter(name='PRODUCTOR').exists()

def ValidarUsuario(request):
    """"
    metodo que redirige a las vista de usuario dependiendo del rol asociado al request.user
    """
    if request.user.is_authenticated:

        if is_administrador(request.user):
            return redirect('administrador')
        elif is_cli_ex(request.user):
            return redirect('cli_ex')
        elif is_cli_in(request.user):
            return redirect('cli_in')

        elif is_trasnp(request.user):
            return redirect('transport')

        elif is_consul(request.user):
            return redirect('consul')
        elif is_productor(request.user):
            return redirect('productor')
        else:
            return redirect('/')

    return redirect('login')



# Create your views here.
def home(request):

    #buscar un usuario y agregarlo a un grupo
    #user = g = User.objects.get(username ='transportista')
    #g = Group.objects.get(name='transportista')
    #g.user_set.add(user)
    
    #x = request.user.check_password('admin')
    

    ValidarUsuario(request)

    g = Group.objects.all()
    data = {
        'grupos': g
    }


    return render(request, 'core/home.html',data)

@user_passes_test(is_administrador)
def home_administrador(request):
    return render(request, 'core/administrador/home-administrador.html')

@user_passes_test(is_cli_ex)
def home_cliente_externo(request):
    return render(request, 'core/cliente_externo/home-cliente-externo.html')

@user_passes_test(is_cli_in)
def home_cliente_iterno(request):
    return render(request, 'core/cliente_interno/home-cliente-interno.html')

@user_passes_test(is_consul)
def home_consultor(request):
    return render(request, 'core/consultor/home-consultor.html')

@user_passes_test(is_trasnp)
def home_trnasportista(request):
    return render(request, 'core/transportista/home-transportista.html')

##############################
#   PRODUCTOR
##############################
@user_passes_test(is_productor)
def home_productor(request):
    
    producto = Producto.objects.filter(user_id = request.user.id)

    data = {
        'producto': producto
    }

    return render(request, 'core/productor/home-productor.html', data)

@user_passes_test(is_productor)
def productor_agregar(request):
    #sin procedure
    calidad = Calidad.objects.all()
    fruta = Fruta.objects.all()

    data = {
        'calidad'   : calidad,
        'fruta'     : fruta 
    }

    if request.POST:
        producto = Producto()
        producto.descripcion = request.POST.get('nombre')
        producto.fecha_subida = request.POST.get('fechaSubida')
        producto.fecha_vencimiento = request.POST.get('fechaVencimiento')
        producto.cantidad = request.POST.get('cantidad')

        calidad = Calidad()
        calidad.id_calidad = request.POST.get('cboCalidad')

        fruta = Fruta()
        fruta.id_fruta = request.POST.get('cboFruta')

        usuario = AuthUser()
        usuario.id = request.user.id

        producto.id_calidad = calidad
        producto.id_fruta =   fruta
        producto.user = usuario

        try:
            producto.save()
            return redirect('productor')
        except:
            data['mensaje'] = 'No se ha podido guardar correctamente'

    return render(request, 'core/productor/producto-agregar.html',data)


@user_passes_test(is_productor)
def productor_actualizar(request, id_producto):

    producto = Producto.objects.get(id_producto=id_producto)
    calidad = Calidad.objects.all()
    fruta = Fruta.objects.all()

    data = {
        'calidad'   : calidad,
        'fruta'     : fruta,
        'producto'  : producto
    }

    if request.POST:
        producto = Producto()
        producto.id_producto = request.POST.get('id_producto')
        producto.descripcion = request.POST.get('nombre')
        producto.fecha_subida = request.POST.get('fechaSubida')
        producto.fecha_vencimiento = request.POST.get('fechaVencimiento')
        producto.cantidad = request.POST.get('cantidad')

        calidad = Calidad()
        calidad.id_calidad = request.POST.get('cboCalidad')

        fruta = Fruta()
        fruta.id_fruta = request.POST.get('cboFruta')

        usuario = AuthUser()
        usuario.id = request.user.id

        producto.id_calidad = calidad
        producto.id_fruta =   fruta
        producto.user = usuario

        try:
            producto.save()
            return redirect('productor') 
        except:
            data['mensaje'] = 'No se ha podido actualizar correctamente'

    return render(request, 'core/productor/producto_modificar.html',data)

@user_passes_test(is_productor)
def producto_eliminar(request, id_producto):

    producto = Producto.objects.get(id_producto=id_producto)
    
    try:
        producto.delete()
    except:
        pass

    return redirect('productor') 

#Formulario Afiliacion
def formulario_afiliacion(request):
    
    if request.POST:
        #crear intancia vacia
        solicitud_afiliacion = []
        #asignacion  variable como parametros 
        #primero los parametros obligaorios
        solicitud_afiliacion.append(request.POST.get('txtNombreCompleto'))
        solicitud_afiliacion.append(request.POST.get('txtmail'))
        solicitud_afiliacion.append(request.POST.get('cboAfiliacion'))

        #vemos si son opcionales en ese caso se agregara un None para que el procedimieto lo tome como null
        temp = None if len(request.POST.get('txtNombreEmpresa'))==0 else request.POST.get('txtNombreEmpresa')
        solicitud_afiliacion.append(temp)

        temp = None if len(request.POST.get('txtComentario'))==0 else request.POST.get('txtComentario')
        solicitud_afiliacion.append(temp)

        temp = None if len(request.POST.get('txtTelefono'))==0 else request.POST.get('txtTelefono')
        solicitud_afiliacion.append(temp)

        agregar_solicitud_afiliacion(solicitud_afiliacion)


    data = {
        'afiliacion' : listado_tipoAfiliacion()
    }
    return render(request, 'core/formulario_afiliacion.html',data)



#cursores
def listado_tipoAfiliacion():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_LISTAR_TIPO_AFILIACION", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def agregar_solicitud_afiliacion(_p):
    """_p[0] = P_NOMBRE_COMPLETO
    """
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc('SP_CREATE_SOLICITUD_AFILIACION',[_p[0],_p[1],_p[2],_p[3],_p[4],_p[5]])


from django.http import JsonResponse
def prueba_login_found(request):
    
    print('esto:',request)
    data = {"a":True}


    return JsonResponse(data)
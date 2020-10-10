from django.contrib import admin
from .models import Fruta, Calidad, Producto
# Register your models here.
class FrutaAdmin(admin.ModelAdmin):
    #declaramos una tupla
    list_display = ('id_fruta','nombre')
admin.site.register(Fruta,FrutaAdmin)

class CalidadAdmin(admin.ModelAdmin):
    #declaramos una tupla
    list_display = ('id_calidad','nombre')
admin.site.register(Calidad,CalidadAdmin)

class ProductoAdmin(admin.ModelAdmin):
    #declaramos una tupla
    list_display = ('id_producto','descripcion','fecha_subida','fecha_vencimiento','id_fruta','id_calidad','cantidad','user')
admin.site.register(Producto,ProductoAdmin)



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    
    def __str__(self):
        return self.username


class Calidad(models.Model):
    id_calidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'calidad'

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    id_cargo = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cargo'


class ClaseLicencia(models.Model):
    id_clase_licencia = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'clase_licencia'


class Conductor(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    num_licencia = models.CharField(max_length=15)
    num_documento = models.IntegerField()
    id_clase_licencia = models.ForeignKey(ClaseLicencia, models.DO_NOTHING, db_column='id_clase_licencia')

    class Meta:
        managed = False
        db_table = 'conductor'


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')
    empleado_user = models.ForeignKey('Empleado', models.DO_NOTHING)
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')

    class Meta:
        managed = False
        db_table = 'contrato'


class CostoProceso(models.Model):
    id_costo_proceso = models.AutoField(primary_key=True)
    valor_transporte = models.BigIntegerField()
    valor_producto_total = models.BigIntegerField()
    aduana = models.BigIntegerField(blank=True, null=True)
    valor_embarque = models.BigIntegerField(blank=True, null=True)
    valor_total_global = models.BigIntegerField()
    id_proceso_venta = models.ForeignKey('ProcesoVenta', models.DO_NOTHING, db_column='id_proceso_venta')

    class Meta:
        managed = False
        db_table = 'costo_proceso'


class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud')
    id_fruta = models.ForeignKey('Fruta', models.DO_NOTHING, db_column='id_fruta')
    id_saldo = models.ForeignKey('Saldo', models.DO_NOTHING, db_column='id_saldo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DetalleTransporte(models.Model):
    id_detalle_trasporte = models.AutoField(primary_key=True)
    valor = models.BigIntegerField(blank=True, null=True)
    id_proceso_venta = models.ForeignKey('ProcesoVenta', models.DO_NOTHING, db_column='id_proceso_venta')

    class Meta:
        managed = False
        db_table = 'detalle_transporte'



class Empleado(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    fecha_contratacion = models.DateField()
    fecha_nacimeinto = models.DateField()
    rut = models.FloatField(unique=True)
    dv = models.FloatField()
    direccion = models.CharField(max_length=100)
    id_genero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='id_genero')
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    email_contacto = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=100)
    id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pais')
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empresa'


class EstadoContrato(models.Model):
    id_estado_contrato = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_contrato'


class EstadoOfertaSubasta(models.Model):
    id_estado_oferta_subasta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'estado_oferta_subasta'


class EstadoProcesoVenta(models.Model):
    id_estado_proceso_venta = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_proceso_venta'


class EstadoSolicitud(models.Model):
    id_estado_solicitud = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_solicitud'


class EstadoSolicitudAfilacion(models.Model):
    id_estado_solicitud = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_solicitud_afilacion'


class Fruta(models.Model):
    id_fruta = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'fruta'
    
    def __str__(self):
        return self.nombre


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'genero'


class OfertaSubastaProducto(models.Model):
    id_ferta_producto = models.AutoField(primary_key=True)
    valor = models.BigIntegerField()
    fecha_oferta = models.DateField()
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_estado_oferta_subasta = models.ForeignKey(EstadoOfertaSubasta, models.DO_NOTHING, db_column='id_estado_oferta_subasta')
    id_subasta_producto = models.ForeignKey('SubastaProducto', models.DO_NOTHING, db_column='id_subasta_producto')

    class Meta:
        managed = False
        db_table = 'oferta_subasta_producto'


class OfertaSubastaTransporte(models.Model):
    id_oferta_subasta_transporte = models.AutoField(primary_key=True)
    valor = models.BigIntegerField()
    fecha_oferta = models.DateField()
    id_subasta_transporte = models.ForeignKey('SubastaTransporte', models.DO_NOTHING, db_column='id_subasta_transporte')
    user = models.ForeignKey(Conductor, models.DO_NOTHING)
    id_estado_oferta_subasta = models.ForeignKey(EstadoOfertaSubasta, models.DO_NOTHING, db_column='id_estado_oferta_subasta')

    class Meta:
        managed = False
        db_table = 'oferta_subasta_transporte'


class Pais(models.Model):
    id_pais = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    two_char_id_pais = models.CharField(max_length=2)
    three_char_id_pais = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'pais'


class ProcesoVenta(models.Model):
    id_proceso_venta = models.AutoField(primary_key=True)
    id_estado_proceso_venta = models.ForeignKey(EstadoProcesoVenta, models.DO_NOTHING, db_column='id_estado_proceso_venta')
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud')

    class Meta:
        managed = False
        db_table = 'proceso_venta'


class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    fecha_subida = models.DateField()
    fecha_vencimiento = models.DateField()
    id_fruta = models.ForeignKey(Fruta, models.DO_NOTHING, db_column='id_fruta')
    id_calidad = models.ForeignKey(Calidad, models.DO_NOTHING, db_column='id_calidad')
    cantidad = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.descripcion


class RangoPrecioTransporte(models.Model):
    id_rango_transporte = models.FloatField(primary_key=True)
    valor_inferior = models.IntegerField()
    valor_superior = models.IntegerField()
    precio_rango = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rango_precio_transporte'


class Rechazo(models.Model):
    id_rechazo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=120)
    id_proceso_venta = models.ForeignKey(ProcesoVenta, models.DO_NOTHING, db_column='id_proceso_venta')
    id_tipo_rechazo = models.ForeignKey('TipoRechazo', models.DO_NOTHING, db_column='id_tipo_rechazo')

    class Meta:
        managed = False
        db_table = 'rechazo'


class Saldo(models.Model):
    id_saldo = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    valor_saldo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saldo'


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50)
    comentario = models.CharField(max_length=120, blank=True, null=True)
    is_nacional = models.BooleanField(blank=True, null=True)
    fecha_creacion = models.DateField()
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pais')
    id_estado_solicitud = models.ForeignKey(EstadoSolicitud, models.DO_NOTHING, db_column='id_estado_solicitud')
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'solicitud'


class SolicitudAfilacion(models.Model):
    id_solicitud = models.SmallAutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=200, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=18, blank=True, null=True)
    mail = models.CharField(max_length=50)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    fecha_solicitud = models.DateField()
    id_estado_solicitud = models.ForeignKey(EstadoSolicitudAfilacion, models.DO_NOTHING, db_column='id_estado_solicitud')
    id_tipo_afiliacion = models.ForeignKey('TipoAfiliacion', models.DO_NOTHING, db_column='id_tipo_afiliacion')
    user = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_afilacion'


class SubastaProducto(models.Model):
    id_subasta_producto = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True)
    id_proceso_venta = models.ForeignKey(ProcesoVenta, models.DO_NOTHING, db_column='id_proceso_venta')
    id_detalle_pedido = models.ForeignKey(DetallePedido, models.DO_NOTHING, db_column='id_detalle_pedido')

    class Meta:
        managed = False
        db_table = 'subasta_producto'


class SubastaTransporte(models.Model):
    id_subasta_transporte = models.AutoField(primary_key=True)
    is_sobrecargo = models.BooleanField()
    is_refrigerador = models.BooleanField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True)
    id_detalle_trasporte = models.ForeignKey(DetalleTransporte, models.DO_NOTHING, db_column='id_detalle_trasporte')

    class Meta:
        managed = False
        db_table = 'subasta_transporte'


class TipoAfiliacion(models.Model):
    id_tipo_afiliacion = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_afiliacion'


class TipoRechazo(models.Model):
    id_tipo_rechazo = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_rechazo'


class TipoVehiculo(models.Model):
    id_tipo_vehiculo = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'


class Vehiculo(models.Model):
    id_vehiculo = models.SmallAutoField(primary_key=True)
    patente = models.CharField(max_length=7)
    capacidad_carga = models.IntegerField()
    sobrecarga = models.BooleanField()
    id_tipo_vehiculo = models.ForeignKey(TipoVehiculo, models.DO_NOTHING, db_column='id_tipo_vehiculo')
    user = models.ForeignKey(Conductor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehiculo'

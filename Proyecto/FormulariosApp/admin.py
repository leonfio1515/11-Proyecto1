from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from rangefilter.filter import DateRangeFilter

from django.conf import settings

from import_export import fields
from import_export.widgets import ForeignKeyWidget

admin.site.site_header="Administrador"

###############################################################################

class PedidoCompraResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')


    num_fun = fields.Field(column_name='Numero funcionario', attribute='num_fun',widget=ForeignKeyWidget(Funcionarios, field='numero_funcionario'))
    nombre_fun = fields.Field(column_name='Nombre funcionario', attribute='nombre_fun')
    ci_fun = fields.Field(column_name='Ci funcionario', attribute='ci_fun')
    importe = fields.Field(column_name='Importe', attribute='importe')
    cuotas = fields.Field(column_name='Cuotas', attribute='cuotas')
    num_factura = fields.Field(column_name='Numero factura', attribute='num_factura')

    class Meta:
        model = PedidoCompra

class PedidoCompraAdmin(ImportExportActionModelAdmin):
    resource_class = PedidoCompraResource
    list_display = (
        "usuario",
        "fecha_registro",

        "num_fun",
        "nombre_fun",
        "ci_fun",
        "importe",
        "cuotas",
        "importe_cuota",
        "num_factura",
        "id"
    )
    search_fields = (
        "num_fun",
        "nombre_fun",
        "ci_fun",
        "importe",
        "cuotas",
        "num_factura",
    )
    list_per_page = 25
    exclude = ("usuario","user_create")
    list_filter = (("date_create",DateRangeFilter),)

    def fecha_registro(self, obj):
        return obj.date_create.strftime('%d/%m/%Y')


class PedidoPapeleriaResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')

    Fecha_enviado = fields.Field(column_name='Fecha_enviado', attribute='Fecha_enviado')
    Lapiceras = fields.Field(column_name='Lapiceras', attribute='Lapiceras')
    Clips = fields.Field(column_name='Clips', attribute='Clips')
    Lapiz = fields.Field(column_name='Lapiz', attribute='Lapiz')
    Grapas = fields.Field(column_name='Grapas', attribute='Grapas')
    ResmaA4 = fields.Field(column_name='ResmaA4', attribute='ResmaA4')
    Sobre_carta = fields.Field(column_name='Sobre_carta', attribute='Sobre_carta')
    Tijera = fields.Field(column_name='Tijera', attribute='Tijera')
    Banda_elastica = fields.Field(column_name='Banda_elastica', attribute='Banda_elastica')
    Comentarios = fields.Field(column_name='Comentarios', attribute='Comentarios')

    class Meta:
        model = PedidoPapeleria

class PedidoPapeleriaAdmin(ImportExportActionModelAdmin):
    resource_class = PedidoPapeleriaResource
    list_display = (
        "usuario",
        "fecha_registro",

        "Fecha_enviado",
        "Lapiceras",
        "Clips",
        "Lapiz",
        "Grapas",
        "ResmaA4",
        "Sobre_carta",
        "Tijera",
        "Banda_elastica",
        "Comentarios",
    )
    search_fields = (
        "usuario",
        "fecha_registro",

        "Fecha_enviado",
        "Lapiceras",
        "Clips",
        "Lapiz",
        "Grapas",
        "ResmaA4",
        "Sobre_carta",
        "Tijera",
        "Banda_elastica",
        "Comentarios",
    )
    list_editable = (
        "Fecha_enviado",
        "Lapiceras",
        "Clips",
        "Lapiz",
        "Grapas",
        "ResmaA4",
        "Sobre_carta",
        "Tijera",
        "Banda_elastica",
        "Comentarios",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update")
    list_filter = (("date_create", DateRangeFilter),)

    def fecha_registro(self, obj):
        return obj.date_create.strftime('%d/%m/%Y')


class AvisaRetiroResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')

    ci_cliente = fields.Field(column_name='CI Cliente', attribute='ci_cliente')
    nombre_cliente = fields.Field(column_name='Nombre cliente', attribute='nombre_cliente')
    producto = fields.Field(column_name='Articulo', attribute='articulo')
    num_factura = fields.Field(column_name='Numero documento', attribute='num_doc')
    suc_retirar = fields.Field(column_name='Sucursal Retirar', attribute='suc_retirar',widget=ForeignKeyWidget(Sucursales, field='ususuarioername'))
    fecha_retiro = fields.Field(column_name='Fecha retiro', attribute='fecha_retiro')
    estado = fields.Field(column_name='Estado', attribute='estado')

    class Meta:
        model = AvisaRetiro
    
class AvisaRetiroAdmin(ImportExportActionModelAdmin):
    resource_class = AvisaRetiroResource
    list_display = (
        "usuario",
        "fecha_registro",
        "ci_cliente",
        "nombre_cliente",
        "producto",
        "num_factura",
        "suc_retirar",
        "fecha_retiro",
        "estado",
        "id",
    )
    search_fields = (
        "usuario__username",
        "date_create",
        "ci_cliente",
        "nombre_cliente",
        "producto",
        "num_factura",
        "suc_retirar__numero_suc",
        "fecha_retiro",
        "estado",
    )
    list_editable = ("estado", "fecha_retiro",)
    list_filter = ("estado", ("date_create", DateRangeFilter),)
    list_per_page = 25
    exclude = (
        "usuario","user_update"
    )

    def fecha_registro(self, obj):
        return obj.date_create.strftime('%d/%m/%Y')



###############################################################################
###############################################################################
###############################################################################
admin.site.register(PedidoPapeleria, PedidoPapeleriaAdmin)
admin.site.register(AvisaRetiro, AvisaRetiroAdmin)
admin.site.register(PedidoCompra, PedidoCompraAdmin)

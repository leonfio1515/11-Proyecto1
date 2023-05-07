from django.contrib import admin
from .models import *
from FormulariosApp.models import *

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from rangefilter.filter import DateRangeFilter

from import_export import fields
from import_export.widgets import ForeignKeyWidget

admin.site.site_header="Administrador"

#############################################################################################
#############################################################################################


class MedioPagoResource(resources.ModelResource):
    class Meta:
        model = MediosPago

class MedioPagoAdmin(ImportExportActionModelAdmin):
    resource_class = MedioPagoResource
    list_display = (
        "usuario",
        "date_create",

        "nombre_pago",
        "id",
    )
    search_fields = (
        "nombre_pago",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


class PlataformaResource(resources.ModelResource):
    class Meta:
        model = Plataforma

class PlataformaAdmin(ImportExportActionModelAdmin):
    resource_class = PlataformaResource
    list_display = (
        "usuario",
        "date_create",

        "plataforma",
        "id",
    )
    search_fields = (
        "plataforma",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


class MotivoDevResource(resources.ModelResource):
    class Meta:
        model = MotivoDev

class MotivoDevAdmin(ImportExportActionModelAdmin):
    resource_class = MotivoDevResource
    list_display = (
        "usuario",
        "date_create",

        "motivoDevolucion",
        "id",
    )
    search_fields = (
        "motivoDevolucion",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


class SucursalesResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')

    usuario = fields.Field(column_name='Usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    numero_suc = fields.Field(column_name='Numero suc', attribute='numero_suc')
    direccion_suc = fields.Field(column_name='Dproveproveireccion', attribute='direccion_suc')
    departamento_suc = fields.Field(column_name='Departamento', attribute='departamento_suc')
    zona_suc = fields.Field(column_name='Zona', attribute='zona_suc')
    encargado_suc = fields.Field(column_name='Encargado', attribute='encargado_suc')
    tel_suc = fields.Field(column_name='Telefono', attribute='tel_suc')
    cod_anda = fields.Field(column_name='cod_anda', attribute='cod_anda')
    cod_cabal = fields.Field(column_name='cod_cabal', attribute='cod_cabal')
    cod_club = fields.Field(column_name='cod_club', attribute='cod_club')
    cod_creditel = fields.Field(column_name='cod_creditel', attribute='cod_creditel')
    cod_creditosD = fields.Field(column_name='cod_creditosD', attribute='cod_creditosD')
    cod_diners = fields.Field(column_name='cod_diners', attribute='cod_diners')
    cod_lider = fields.Field(column_name='cod_lider', attribute='cod_lider')
    cod_maestro = fields.Field(column_name='cod_maestro', attribute='cod_maestro')
    cod_master = fields.Field(column_name='cod_master', attribute='cod_master')
    cod_sodexo = fields.Field(column_name='cod_sodexo', attribute='cod_sodexo')
    cod_oca = fields.Field(column_name='cod_oca', attribute='cod_oca')
    cod_passcard = fields.Field(column_name='cod_passcard', attribute='cod_passcard')
    cod_visa = fields.Field(column_name='cod_visa', attribute='cod_visa')
    cod_tarjetad = fields.Field(column_name='cod_tarjetad', attribute='cod_tarjetad')
    cod_edenred = fields.Field(column_name='cod_edenred', attribute='cod_edenred')
    cod_retop = fields.Field(column_name='cod_retop', attribute='cod_retop')
    user_retop = fields.Field(column_name='user_retop', attribute='user_retop')
    pass_retop = fields.Field(column_name='pass_retop', attribute='pass_retop')
    cod_pronto = fields.Field(column_name='cod_pronto', attribute='cod_pronto')
    user_pronto = fields.Field(column_name='user_pronto', attribute='user_pronto')
    pass_pronto = fields.Field(column_name='pass_pronto', attribute='pass_pronto')
    cod_inforcheck = fields.Field(column_name='cod_inforcheck', attribute='cod_inforcheck')
    suc_inforcheck = fields.Field(column_name='suc_inforcheck', attribute='suc_inforcheck')
    clave_inforcheck = fields.Field(column_name='clave_inforcheck', attribute='clave_inforcheck')
    user_taxfree = fields.Field(column_name='user_taxfree', attribute='user_taxfree')
    pass_taxfree = fields.Field(column_name='pass_taxfree', attribute='pass_taxfree')

    class Meta:
        model = Sucursales

class SucursalesAdmin(ImportExportActionModelAdmin):
    resource_class = SucursalesResource
    list_display = (
        "date_create",

        "numero_suc",
        "direccion_suc",
        "departamento_suc",
        "id"
    )
    search_fields = (
        "numero_suc",
        "direccion_suc",
        "departamento_suc",
        "usuario",
    )
    list_per_page = 25
    exclude = ("user_create", "user_update",)



class MensajesResource(resources.ModelResource):
    class Meta:
        model = Mensajes

class MensajesAdmin(ImportExportActionModelAdmin):
    resource_class = MensajesResource
    list_display = (
        "usuario",
        "date_create",

        "nombre",
        "asunto",
    )
    search_fields = (
        "nombre",
        "asunto",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


class ComunicacionesResource(resources.ModelResource):
    class Meta:
        model = Comunicaciones


class ComunicacionesAdmin(ImportExportActionModelAdmin):
    resource_class = ComunicacionesResource
    list_display = (
        "usuario",
        "date_create",

        "medio_promo",
        "valor_promo",
        "fecha_inicio",
        "fecha_fin",
        "alcance_promo",
        "estado_promo",
    )
    search_fields = (
        "medio_promo",
        "valor_promo",
        "fecha_inicio",
        "fecha_fin",
        "estado_promo",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)



class GrupoErrorResource(resources.ModelResource):
    class Meta:
        model = GrupoError

class GrupoErrorAdmin(ImportExportActionModelAdmin):
    resource_class = GrupoErrorResource
    list_display = (
        "usuario",
        "date_create",

        "nombre",
    )
    search_fields = (
        "usuario",
        "date_create",
        "nombre",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)



class CargoFuncioanrioResource(resources.ModelResource):
    class Meta:
        model = CargoFuncionario

class CargoFuncioanrioAdmin(ImportExportActionModelAdmin):
    resource_class = CargoFuncioanrioResource
    list_display = (
        "usuario",
        "date_create",

        "nombre_cargo",
        "id",

   )
    search_fields = (
       "nombre_cargo",
   )
    list_per_page = 25
    exclude = ("usuario", "user_update",)



class FraudesResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')

    plataforma = fields.Field(column_name='Plataforma', attribute='plataforma',widget=ForeignKeyWidget(Plataforma, field='plataforma'))
    num_pedido = fields.Field(column_name='Numero pedido', attribute='num_pedido')
    forma_pago = fields.Field(column_name='Forma de pago', attribute='forma_pago',widget=ForeignKeyWidget(MediosPago, field='nombre_pago'))
    importe = fields.Field(column_name='Importe', attribute='importe')
    ci_cliente = fields.Field(column_name='CI cliente', attribute='ci_cliente')
    num_factura = fields.Field(column_name='Numero factura', attribute='num_factura')
    num_nc = fields.Field(column_name='Numero NC', attribute='num_nc')
    estado_mercaderia = fields.Field(column_name='Estado mercaderia', attribute='estado_mercaderia')
    estado_pago = fields.Field(column_name='Estado pago', attribute='estado_pago')
    liq_descuento = fields.Field(column_name='Liquidacion descuento', attribute='liq_descuento')

    class Meta:
        model = RegistroFraudes

class FraudesAdmin(ImportExportActionModelAdmin):
    resource_class = FraudesResource
    list_display = (
        "usuario",
        "date_create",

        "plataforma",
        "num_pedido",
        "forma_pago",
        "importe",
        "ci_cliente",
        "num_factura",
        "num_nc",
        "estado_mercaderia",
        "estado_pago",
        "liq_descuento",
    )
    search_fields = (
        "usuario",
        "date_create",
        "plataforma",
        "num_pedido",
        "forma_pago",
        "importe",
        "ci_cliente",
        "num_factura",
        "num_nc",
        "estado_mercaderia",
        "estado_pago",
        "liq_descuento",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


class FinancieraResource(resources.ModelResource):
    class Meta:
        model = Financieras

class FinancieraAdmin(ImportExportActionModelAdmin):
    resource_class = FinancieraResource
    list_display = (
        "usuario",
        "date_create",

        "nombre_financiera",
        "tel_contacto",
        "email_contacto",
    )
    search_fields = (
        "usuario",
        "date_create",
        "nombre_financiera",
        "tel_contacto",
        "email_contacto",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)



class AreaResource(resources.ModelResource):
    class Meta:
        model = Area
    
class AreaAdmin(ImportExportActionModelAdmin):
    resource_class = AreaResource
    list_display = (
        "nombre",
    )
    search_fields = (
        "nombre",
    )
    list_per_page = 25
    exclude = (
        "usuario","user_update"
    )


###############################################################################



###############################################################################
admin.site.register(MediosPago, MedioPagoAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(MotivoDev, MotivoDevAdmin)
admin.site.register(Sucursales, SucursalesAdmin)


admin.site.register(Mensajes, MensajesAdmin)

admin.site.register(GrupoError, GrupoErrorAdmin)
admin.site.register(CargoFuncionario, CargoFuncioanrioAdmin)


admin.site.register(RegistroFraudes, FraudesAdmin)
admin.site.register(Financieras, FinancieraAdmin)

admin.site.register(Area, AreaAdmin)

###############################################################################

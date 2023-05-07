from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from rangefilter.filter import DateRangeFilter

from import_export import fields
from import_export.widgets import ForeignKeyWidget

################################################################

class FuncionariosResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')

    numero_funcionario=fields.Field(column_name='Numero fun',attribute='numero_funcionario')
    nombre_funcionario=fields.Field(column_name='Nombre fun',attribute='nombre_funcionario')
    apellido_funcionario=fields.Field(column_name='Apellido fun',attribute='apellido_funcionario')
    cedula_funcionario=fields.Field(column_name='CI fun',attribute='cedula_funcionario')
    cargo_funcionario=fields.Field(column_name='Cargo',attribute='cargo_funcionario',widget=ForeignKeyWidget(CargoFuncionario, field='nombre_cargo'))
    sexo_funcionario=fields.Field(column_name='Sexo',attribute='sexo_funcionario')
    fecha_ingreso=fields.Field(column_name='Fecha ingreso',attribute='fecha_ingreso')
    estado_funcionario=fields.Field(column_name='Estado',attribute='estado_funcionario')
    disponible_funcionario=fields.Field(column_name='Disponible',attribute='disponible_funcionario')
    sucursal=fields.Field(column_name='Sucursal',attribute='sucursal',widget=ForeignKeyWidget(Sucursales, field='numero_suc'))

    class Meta:
        model = Funcionarios
        import_id_fields = ('numero_funcionario',)

class FuncionariosAdmin(ImportExportActionModelAdmin):
    resource_class = FuncionariosResource
    list_display = (
        "user_update",
        "date_create",

        "numero_funcionario",
        "nombre_funcionario",
        "apellido_funcionario",
        "cedula_funcionario",
        "cargo_funcionario",
        "sexo_funcionario",
        "fecha_ingreso",
        "estado_funcionario",
        "sucursal",
        "disponible_funcionario",

    )
    search_fields = (
        "nombre_funcionario",
        "apellido_funcionario",
        "cedula_funcionario",
        "numero_funcionario",
        "cargo_funcionario__nombre_cargo",
        "sexo_funcionario",
        "fecha_ingreso",
        "estado_funcionario",
        "disponible_funcionario",
    )
    list_editable = ["disponible_funcionario","sucursal","estado_funcionario"]
    list_filter = ("estado_funcionario", "cargo_funcionario",)
    list_per_page = 25
    exclude = ("user_update", "usuario","limite_saldo","disponible_funcionario")



################################################################

admin.site.register(Funcionarios, FuncionariosAdmin)


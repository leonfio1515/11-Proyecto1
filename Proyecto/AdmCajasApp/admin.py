from django.contrib import admin
from .models import *


from import_export import resources
from rangefilter.filter import DateRangeFilter
from import_export.admin import ImportExportActionModelAdmin

from import_export import fields
from import_export.widgets import ForeignKeyWidget

############################################################################################
class ManualesResource(resources.ModelResource):
    class Meta:
        model = Manuales

class ManualesAdmin(ImportExportActionModelAdmin):
    resource_class = ManualesResource
    list_display = (
        "usuario",
        "date_create",
        
        "nombre_manual",
    )
    search_fields = (
        "nombre_manual",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


class ErroresResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    usuario = fields.Field(column_name='usuario', attribute='usuario',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    user_update = fields.Field(column_name='Usuario edicion', attribute='user_update',widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    date_create = fields.Field(column_name='Fecha registro', attribute='date_create')
    date_update = fields.Field(column_name='Fecha edicion', attribute='date_update')

    sucursal = fields.Field(column_name='Sucursal', attribute='sucursal',widget=ForeignKeyWidget(Sucursales, field='usuario'))
    fecha_error = fields.Field(column_name='Fecha error', attribute='fecha_error')
    num_cajera = fields.Field(column_name='Numero cajera', attribute='num_cajera')
    num_boleta = fields.Field(column_name='Numero boleta', attribute='num_boleta')
    grupo = fields.Field(column_name='Grupo', attribute='grupo',widget=ForeignKeyWidget(GrupoError, field='nombre'))
    comentario = fields.Field(column_name='Comentario', attribute='comentario')

    class Meta:
        model=Errores

class ErroresAdmin(ImportExportActionModelAdmin):
    resource_class = ErroresResource
    list_display = (
        "usuario",
        "date_create",

        "sucursal",
        "fecha_error",
        "num_cajera",
        "num_boleta",
        "grupo",
        "comentario",
    )
    search_fields = (
        "sucursal__usuario__username",
        "fecha_error",
        "num_cajera",
        "num_boleta",
        "grupo__nombre",
        "comentario",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)
    list_filter = ("grupo","usuario",("date_create",DateRangeFilter))

############################################################################################
admin.site.register(Manuales, ManualesAdmin)
admin.site.register(Errores, ErroresAdmin)

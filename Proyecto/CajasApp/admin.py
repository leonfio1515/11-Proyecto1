from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from import_export import fields
from import_export.widgets import ForeignKeyWidget
###################################################################################



class PreguntasFrecResource(resources.ModelResource):

    class Meta:
        model = PreguntasFrec

class PreguntasFrecAdmin(ImportExportActionModelAdmin):
    list_display = (
        "nombre",
        "date_create",
        "usuario",
    )
    search_fields = (
        "nombre",
        "date_create",
        "usuario",
    )
    list_per_page = 25
    exclude = ("usuario", "user_update",)


####################################################################################
####################################################################################
####################################################################################

admin.site.register(PreguntasFrec, PreguntasFrecAdmin)

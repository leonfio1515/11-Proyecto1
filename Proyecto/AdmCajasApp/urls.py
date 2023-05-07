from django.urls import path
from .views import *

####################################################################################################

urlpatterns = [
    ########## LIST ###########

    path('registro_errores_list', RegistroErroresList.as_view(),name='registro_errores_list'),
    path('manuales_list_adm', ManualesList.as_view(),name='manuales_list_adm'),
    path('comunicaciones_list_adm', ComunicacionesAdmList.as_view(),
         name='comunicaciones_list_adm'),

]

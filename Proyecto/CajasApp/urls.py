from django.urls import path
from .views import *

#############################################################################################


urlpatterns = [


    ################ MANUALES ##################################
    path('manuales_list', ManualesView.as_view(), name="manuales_list"),
    path(r'manual_detalle/<int:pk>',ManualesDetail.as_view(), name="manual_detalle"),

    ################ PROCESOS ##################################
    path('preguntas_frecuentes', PreguntasFrecList.as_view(), name="preguntas_frecuentes"),
]

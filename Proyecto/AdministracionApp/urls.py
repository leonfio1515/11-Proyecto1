from django.urls import path
from .views import *


urlpatterns = [
    ######### CREATE #########
    path('mensaje_create', MensajeCreate.as_view(), name='mensaje_create'),
    path('fraudes_create', FraudesCreate.as_view(), name='fraudes_create'),


    ######### LIST #########
    path('fraudes_list', FraudesList.as_view(), name='fraudes_list'),

    path('pedido_compra_adm_personal_list', PedidoCompraAdmPersonalList.as_view(
    ), name="pedido_compra_adm_personal_list"),


    ######### UPDATE #########
    path('fraudes_update/<int:pk>',FraudesUpdate.as_view(), name='fraudes_update'),


]

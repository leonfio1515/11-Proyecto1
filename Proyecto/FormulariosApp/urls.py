from django.urls import path
from .views import *

#########################################################################################


urlpatterns = [
    ####### CRTEATE #############
    path('pedido_compra_create', PedidoCompraCreate.as_view(),
         name='pedido_compra_create'),
    path('pedido_papeleria_create', PapeleriaCreate.as_view(),name='pedido_papeleria_create'),
    path('avisa_retiro_create', AvisoRetiroCreate.as_view(),
         name="avisa_retiro_create"),


    ####### LIST #############
    path('pedido_compra_list', PedidoCompraList.as_view(),
         name="pedido_compra_list"),
    path('pedido_papeleria_list', PapeleriaList.as_view(), name="pedido_papeleria_list"),
    path('mensajes_list', MensajesList.as_view(), name="mensajes_list"),
    path('avisa_retiro_list', AvisaRetiroList.as_view(),name="avisa_retiro_list"),
    path('avisa_retiro_suc_list', AvisaRetiroSucList.as_view(),name="avisa_retiro_suc_list"),

    ####### UPDATE #############
    path('pedido_compra_update/<int:pk>',
         PedidoCompraUpdate.as_view(), name='pedido_compra_update'),
    path('avisa_retiro_update/<int:pk>',AvisaRetiroUpdate.as_view(), name='avisa_retiro_update'),


    ####### DETAIL #############
    path('pedido_compra_detail/<int:pk>',
         PedidoCompraDetail.as_view(), name="pedido_compra_detail"),
    path('pedido_papeleria_detail/<int:pk>',PapeleriaDetail.as_view(), name="pedido_papeleria_detail"),
    path('mensajes_detail/<int:pk>', MensajesDetail.as_view(), name="mensajes_detail"),


    ####### PRINT #############
    path('avisa_retiro_print/<int:pk>',
         AvisaRetiroPrint.as_view(), name="avisa_retiro_print"),


]

from django.contrib import admin
from django.urls import path, include

from .views import *
from django.conf import settings
from django.conf.urls.static import static
###################################################################################

urlpatterns = [
    path('admin/', admin.site.urls, name="admin/"),

    path('Proy/cajas/', include('CajasApp.urls')),
    path('Proy/formularios/', include('FormulariosApp.urls')),
    path('Proy/admCajas/', include('AdmCajasApp.urls')),
    path('Proy/adm/', include('AdministracionApp.urls')),

    path('inicio', InicioView.as_view(), name='inicio'),
    path('sucursales', SucursalesList.as_view(), name='sucursales'),
  
    path('sesion_group/<int:pk>/', SesionGroupView.as_view(), name='sesion_group'),
    path('data_user', DatosUserList.as_view(), name='data_user'),
        
    path('login/', include('Login.urls')),
    path('', InicioView.as_view(), name='inicio'),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
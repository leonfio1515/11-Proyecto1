from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.models import Group
from datetime import datetime


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from AdministracionApp.models import Sucursales,Comunicaciones
from AdmConveniosApp.models import HabilitaBoton


#######################################################################################################

today = datetime.now()
error = {"Debe completar todos los campos":"error"}


class InicioView(TemplateView):
    template_name = "inicio.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwars):
        return super().dispatch(request, *args, **kwars)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['promo'] = Comunicaciones.objects.filter(fecha_fin__gte=today, fecha_inicio__lte=today).order_by('-fecha_fin')

        context['habilitaBoton'] = HabilitaBoton.objects.all()

        return context
 
class SucursalesList(ListView):
    model = Sucursales
    template_name = 'sucursales.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwars):
        return super().dispatch(request, *args, **kwars)

    def get_queryset(self):
        return Sucursales.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['title'] = 'Listado de Sucursales'
        return context

class SesionGroupView(View):
    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return redirect('inicio')

class DatosUserList(ListView):
    model = Sucursales
    template_name = "data_user.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        title = ""
        filtro = {}
        if user is False:
            return redirect("inicio")
        else:
            filtro = Sucursales.objects.filter(usuario=user)

        return render(request, self.template_name, {"filtro": filtro, "title": title})


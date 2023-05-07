from django.shortcuts import render,redirect
from datetime import datetime

from django.views.generic.detail import DetailView
from django.views.generic import ListView, UpdateView, TemplateView

from AdmCajasApp.models import Manuales
from CajasApp.models import *

from AdmConveniosApp.models import HabilitaBoton


from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#############################################################################

fechaahora = datetime.now()
error = {"Debe completar todos los campos":"error"}


##################### LIST ########################################
##################### LIST ########################################
##################### LIST ########################################

class ManualesView(TemplateView):
    model = Manuales
    template_name = "List/list_manual.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwars):
        return super().dispatch(request, *args, **kwars)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manuales'] = Manuales.objects.all()
        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['title'] = 'Manuales'
        return context



##################### DETAIL ########################################
##################### DETAIL ########################################
##################### DETAIL ########################################

class ManualesDetail(LoginRequiredMixin, DetailView):
    model = Manuales
    template_name = 'Detail/detail_manual.html'


##################### PROCESOS ########################################
##################### PROCESOS ########################################
##################### PROCESOS ########################################
    
class PreguntasFrecList(ListView):
    model = PreguntasFrec
    template_name = "Procesos/preguntas_frecuentes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = PreguntasFrec.objects.all()
        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['title'] = "Preguntas Frecuentes"
        return context

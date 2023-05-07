from django.shortcuts import redirect, render

from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, TemplateView

from .models import *
from .forms import *
from AdmConveniosApp.models import HabilitaBoton



from Proyecto.mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from datetime import timedelta, date, datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Coalesce
from django.db.models import Sum


###################################################################################################

dia_dif = timedelta(days=-180)
fechahasta = date.today()
fechadesde = fechahasta + dia_dif
today = datetime.now()

####################### CREATE ####################################
####################### CREATE ####################################
####################### CREATE ####################################


class MensajeCreate(CreateView):
    model = Mensajes
    form_class = MensajeForm
    template_name = "Form/form_contacto.html"

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST["action"]
        if action == "add":
            form = self.get_form()
            data = form.save()
        else:
            data["error"] = "No ha ingresado a ninguna opcion"
        return redirect("mensajes_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['title'] = 'Ponte en contacto'
        context['action'] = 'add'
        return context





class FraudesCreate(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    permission_required = "add_registrofraudes"
    model = RegistroFraudes
    form_class = RegistroFraudeForm
    template_name = "Form/form_fraudes.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST["action"]
        if action == "add":
            form = self.get_form()
            data = form.save()
        else:
            data["error"] = "No ha ingresado a ninguna opcion"
        return redirect("fraudes_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro Fraudes'
        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['action'] = 'add'
        return context


####################### LIST ####################################
####################### LIST ####################################
####################### LIST ####################################
class PedidoCompraAdmPersonalList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = ("view_pedidoconvenio", "change_pedidoconvenio")

    model = PedidoCompra
    template_name = "List/list_pedido_convenio_admpersonal.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in PedidoCompra.objects.all():
                    data.append(i.toJSON())
            elif action == 'confirm':
                solconvenio = PedidoCompra.objects.get(pk=request.POST['id'])
                control = request.POST['control_adm']
                control_adm = {}
                if control == "on":
                    control_adm = "True"
                else:
                    control_adm = "False"
                solconvenio.control_adm = control_adm
                solconvenio.save()
                return redirect('pedido_convenios_adm_personal_list')
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            return redirect('pedido_convenios_adm_personal_list')
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = PedidoCompra.objects.all().order_by('date_create')
        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['formConfirm'] = PedidoCompraControlEditForm()

        context['titleConfirm'] = 'Control de Convenio'
        context['title'] = 'Solicitud de Convenio'
        return context



class FraudesList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = "view_registrofraudes"
    model = RegistroFraudes
    template_name = "List/list_fraudes.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'graph_bars_ano':
                data = [{
                    'name': datetime.now().year,
                    'data': self.graph_bars_ano()
                }, {
                    'name': datetime.now().year-1,
                    'data': self.graph_bars_ano2()
                }]
            elif action == 'graph_pie_finan':
                data = {
                    'name': 'Segun financiera',
                    'data': self.graph_pie_finan()
                }
            elif action == 'graph_pie_est_pago':
                data = {
                    'name': 'Estado pago',
                    'data': self.graph_pie_est_pago()
                }
            elif action == 'graph_pie_est_entrega':
                data = {
                    'name': 'Estado entrega',
                    'data': self.graph_pie_est_entrega()
                }
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            return redirect('manuales_list_adm')
        return JsonResponse(data, safe=False)

    def graph_pie_finan(self):
        data = []
        for i in MediosPago.objects.all():
            total = RegistroFraudes.objects.filter(forma_pago=i).aggregate(
                r=Coalesce(Sum('importe'), 0)).get('r')
            data.append({
                'name': i.nombre_pago,
                'y': float(total),
            })
        return data

    def graph_pie_est_pago(self):
        estados = {}
        for registro in RegistroFraudes.objects.all():
            estado_pago = registro.estado_pago
            if estado_pago in estados:
                estados[estado_pago] += 1
            else:
                estados[estado_pago] = 1

        data = []
        for estado, cantidad in estados.items():
            data.append({
                'name': estado,
                'y': cantidad,
            })

        return data

    def graph_pie_est_entrega(self):
        estados = {}
        for registro in RegistroFraudes.objects.all():
            estado_mercaderia = registro.estado_mercaderia
            if estado_mercaderia in estados:
                estados[estado_mercaderia] += 1
            else:
                estados[estado_mercaderia] = 1

        data = []
        for estado, cantidad in estados.items():
            data.append({
                'name': estado,
                'y': cantidad,
            })

        return data

    def graph_bars_ano(self):
        data = []
        year = datetime.now().year
        for month in range(1, 13):
            total = RegistroFraudes.objects.filter(fecha_venta__year=year, fecha_venta__month=month).aggregate(
                r=Coalesce(Sum('importe'), 0)).get('r')
            data.append(float(total))
        return data

    def graph_bars_ano2(self):
        data = []
        year = datetime.now().year-1
        for month in range(1, 13):
            total = RegistroFraudes.objects.filter(fecha_venta__year=year, fecha_venta__month=month).aggregate(
                r=Coalesce(Sum('importe'), 0)).get('r')
            data.append(float(total))
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = RegistroFraudes.objects.all().order_by('date_create')
        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['title'] = 'Listado Fraudes'
        return context


#################################################################################################
#################################################################################################


####################### UPDATE ####################################
####################### UPDATE ####################################
####################### UPDATE ####################################


class FraudesUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    permission_required = "change_registrofraudes"
    model = RegistroFraudes
    template_name = "update_fraudes.html"
    form_class = RegistroFraudeEditForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST["action"]
        if action == "edit":
            form = self.get_form()
            data = form.save()
        else:
            data["error"] = "No ha ingresado a ninguna opcion"
        return redirect("fraudes_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['title'] = 'Fraudes'
        context['action'] = 'edit'
        return context



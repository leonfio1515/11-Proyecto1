from django.shortcuts import redirect

from .models import *

from AdmConveniosApp.models import HabilitaBoton

from .forms import *

from django.views.generic import ListView
from django.http import JsonResponse

from Proyecto.mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from AdministracionApp.models import MediosPago

#########################################################################################################################################



################## LIST ####################################
################## LIST ####################################
################## LIST ####################################

class ManualesList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = "view_manuales"
    model = Manuales
    template_name = "List/list_manuales.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Manuales.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                manuales = Manuales()
                manuales.nombre_manual = request.POST['nombre_manual']
                manuales.manual = request.FILES['manual']
                manuales.save()
            elif action == 'edit':
                manuales = Manuales.objects.get(pk=request.POST['id'])
                manual = manuales.manual
                manuales.nombre_manual = request.POST['nombre_manual']
                manuales.manual = manual
                manuales.save()
            elif action == 'delete':
                manuales = Manuales.objects.get(pk=request.POST['id'])
                manuales.delete()

            else:
                data['error']= 'Ha ocurrido un error'
        except Exception as e:
            return redirect('manuales_list_adm')
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = Manuales.objects.all()

        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['formAdd'] = ManualesForm()
        context['formEdit'] = ManualesForm()
        context['title'] = 'Listado Manuales'
        return context
    

class ComunicacionesAdmList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = "view_promociones"
    model = Comunicaciones
    template_name = "List/list_promociones.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
            elif action == 'add':
                medio_promo = MediosPago.objects.get(id=request.POST['medio_promo'])
                comunicaciones = Comunicaciones()
                comunicaciones.medio_promo = medio_promo
                comunicaciones.valor_promo = request.POST['valor_promo']
                comunicaciones.descripcion_promo = request.POST['descripcion_promo']
                comunicaciones.imagen_promo = request.FILES['imagen_promo']
                comunicaciones.fecha_inicio = request.POST['fecha_inicio']
                comunicaciones.fecha_fin = request.POST['fecha_fin']
                comunicaciones.alcance_promo = request.POST['alcance_promo']
                comunicaciones.condiciones_promo = request.POST['condiciones_promo']
                comunicaciones.condiciones2_promo = request.POST['condiciones2_promo']
                comunicaciones.estado_promo = "True"

                comunicaciones.save()
            else:
                data['error']= 'Ha ocurrido un error'
        except Exception as e:
            return redirect('manuales_list_adm')
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = Comunicaciones.objects.all()
        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['formAdd'] = ComunicacionesForm()
        context['formEdit'] = ComunicacionesForm()

        context['title'] = 'Listado Promociones'
        return context



class RegistroErroresList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    permission_required = "view_errores"
    model = Errores
    template_name = "List/list_errores.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Errores.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                sucursal = Sucursales.objects.get(id=request.POST['sucursal'])
                grupo = GrupoError.objects.get(id=request.POST['grupo'])

                errores = Errores()
                errores.sucursal = sucursal
                errores.fecha_error = request.POST['fecha_error']
                errores.num_cajera = request.POST['num_cajera']
                errores.num_boleta = request.POST['num_boleta']
                errores.grupo = grupo
                errores.comentario = request.POST['comentario']
                errores.save()
            elif action == 'edit':
                sucursal = Sucursales.objects.get(id=request.POST['sucursal'])
                grupo = GrupoError.objects.get(id=request.POST['grupo'])

                errores = Errores.objects.get(pk=request.POST['id'])

                errores.sucursal = sucursal
                errores.fecha_error = request.POST['fecha_error']
                errores.num_cajera = request.POST['num_cajera']
                errores.num_boleta = request.POST['num_boleta']
                errores.grupo = grupo
                errores.comentario = request.POST['comentario']
                errores.save()
                return redirect('registro_errores_list')
            elif action == 'delete':
                errores = Errores.objects.get(pk=request.POST['id'])
                errores.delete()
            else:
                data['error']= 'Ha ocurrido un error'
        except Exception as e:
            return redirect('registro_errores_list')
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = Errores.objects.all().order_by('-fecha_error')
        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['formAdd'] = ErroresForm()
        context['formEdit'] = ErroresForm()
        context['formConfirm'] = ErroresForm()

        context['title'] = 'Listado Errores'
        context['action'] = 'add'
        return context


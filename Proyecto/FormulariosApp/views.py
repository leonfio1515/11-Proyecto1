from django.shortcuts import render, redirect

from datetime import timedelta, date

from .models import *
from FormulariosApp.forms import *

from AdministracionApp.models import Mensajes,Sucursales
from AdmConveniosApp.models import HabilitaBoton

from django.views.generic.edit import CreateView
from django.views.generic import ListView , UpdateView
from django.views.generic.detail import DetailView


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

##############################################################################################################

dia_dif = timedelta(days=-180)
dia_difenc = timedelta(days=-7)
fechahasta = date.today()
fechadesde = fechahasta + dia_dif
fechadesdeenc = fechahasta + dia_difenc

#########################  CREATE ######################################################
#########################  CREATE ######################################################
#########################  CREATE ######################################################


class PedidoCompraCreate(CreateView):
    model = PedidoCompra
    form_class = PedidoCompraForm
    template_name = "form_pedido_convenios.html"    

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST["action"]

        form = self.get_form()
        num_fun = form["num_fun"].value()
        importe_compra = form["importe"].value()
        cuotas = form["cuotas"].value()

        fun = Funcionarios.objects.get(numero_funcionario=num_fun)

        imp_cuota = round((int(importe_compra)/int(cuotas)), 2)
        nombre = fun.nombre_funcionario+" "+fun.apellido_funcionario
        ci = fun.cedula_funcionario
        disponible = fun.disponible_funcionario
        disponible_nuevo = ()
        estado_autorizacion = ()
        sol_creada = ()

        if action == "add":
            if imp_cuota < disponible and fun.estado_funcionario == "Activo":
                estado_autorizacion = "Autorizada"
                disponible_nuevo = round(
                    (float(disponible)-float(imp_cuota)), 2)

                fun.disponible_funcionario = disponible_nuevo
                fun.save()

                compra_nueva = PedidoCompra(
                    num_fun=Funcionarios.objects.get(
                        numero_funcionario=num_fun),
                    importe=form["importe"].value(),
                    cuotas=form["cuotas"].value(),
                    importe_cuota=imp_cuota,
                    nombre_fun=nombre,
                    ci_fun=ci,
                )
                compra_nueva.save()
                id_compra = compra_nueva.id
                sol_creada = PedidoCompra.objects.get(id=id_compra)
                return render(request, "resp_convenios.html", {
                    "sol_creada": sol_creada,
                    "num_fun": num_fun,
                    "ci": ci,
                    "fun": fun,
                    "nombre": nombre,
                    "importe_compra": importe_compra,
                    "cuotas": cuotas,
                    "imp_cuota": imp_cuota,
                    "disponible": disponible,
                    "disponible_nuevo": disponible_nuevo,
                    "estado_autorizacion": estado_autorizacion,
                    "disponible_funcionario": disponible_nuevo,
                })
            else:
                estado_autorizacion = "No autorizada"
    
            return render(request, "resp_convenios.html", {
                "num_fun": num_fun,
                "ci": ci,
                "fun": fun,
                "nombre": nombre,
                "importe_compra": importe_compra,
                "cuotas": cuotas,
                "imp_cuota": imp_cuota,
                "disponible": 0,
                "disponible_nuevo": disponible_nuevo,
                "estado_autorizacion": estado_autorizacion,
                "disponible_funcionario": disponible_nuevo,
            })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['title'] = 'Pedido Autorizacion compra'
        context['action'] = 'add'
        return context

class PapeleriaCreate(CreateView):
    model = PedidoPapeleria
    form_class = PapeleriaForm
    template_name = "form_pedido_papeleria.html"

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
        return redirect("pedido_papeleria_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pedido Papeleria'
        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['action'] = 'add'
        return context

class AvisoRetiroCreate(CreateView):
    model = AvisaRetiro
    form_class = AvisaRetiroForm
    template_name = "form_retira_cliente.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST["action"]
        if action == "add":
            form = self.get_form()
            data = form.save()
        else:
            data["error"] = "No ha ingresado a ninguna opcion"
        return redirect("avisa_retiro_suc_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habilitaBoton'] = HabilitaBoton.objects.all()

        context['title'] = 'Aviso de retiro'
        context['action'] = 'add'
        return context

#########################  LIST ######################################################
#########################  LIST ######################################################
#########################  LIST ######################################################

class PedidoCompraList(ListView):
    model = PedidoCompra
    template_name = "List/list_pedido_convenio.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['filtro'] = PedidoCompra.objects.filter(
            usuario=self.request.user)

        context['title'] = 'Pedido de convenio'
        context['action'] = 'add'
        return context

    
class PapeleriaList(ListView):
    model = PedidoPapeleria
    template_name = "List/list_pedido_papeleria.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['filtro'] = PedidoPapeleria.objects.filter(usuario=self.request.user, date_create__gte=fechadesde)

        context['title'] = "Pedido de Papeleria"
        return context

class MensajesList(ListView):
    model = Mensajes
    template_name = "List/list_mensajes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['habilitaBoton'] = HabilitaBoton.objects.all()
        context['filtro'] = Mensajes.objects.filter(usuario=self.request.user)

        context['title'] = 'Mensajes enviados'
        return context
   
class AvisaRetiroList(ListView):
    model = AvisaRetiro
    template_name = "list_retira_cliente.html"

    @method_decorator(login_required)
    def get(self, request,  *args, **kwargs):
        user = request.user.sucursales.numero_suc
        title = "Avisa Retiro"
        suc = Sucursales.objects.get(numero_suc=user)
        filtro = AvisaRetiro.objects.filter(
            suc_retirar=suc).order_by('ci_cliente')
        return render(request, self.template_name, {"filtro": filtro, "title": title})

class AvisaRetiroSucList(ListView):
    model = AvisaRetiro
    template_name = "list_retira_cliente_suc.html"

    @method_decorator(login_required)
    def get(self, request,  *args, **kwargs):
        user = request.user
        title = "Avisa Retiro - Para Imprimir"
        filtro = AvisaRetiro.objects.filter(usuario=user).latest("id")
        return render(request, self.template_name, {"filtro": filtro, "title": title})


#########################  UPDATE ######################################################
#########################  UPDATE ######################################################
#########################  UPDATE ######################################################

class PedidoCompraUpdate(UpdateView):
    model = PedidoCompra
    template_name = "update_pedido_convenio.html"
    form_class = PedidoCompraEditForm

    @method_decorator(login_required)
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
        return redirect("pedido_convenio_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Pedido autorizacion compra'
        context['action'] = 'edit'
        return context

class AvisaRetiroUpdate(UpdateView):
    model = AvisaRetiro
    template_name = "update_retira_cliente.html"
    form_class = AvisaRetiroConfForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST["action"]
        if action == "edit":
            form = self.get_form()
            data = form.save()
            print(form)
        else:
            data["error"] = "No ha ingresado a ninguna opcion"
        return redirect("avisa_retiro_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = AvisaRetiro.objects.get(id=self.object.pk)
        context['title'] = 'Avisa Retiro'
        context['action'] = 'edit'
        return context



#########################  DETAIL ######################################################
#########################  DETAIL ######################################################
#########################  DETAIL ######################################################

class PedidoCompraDetail(DetailView):
    model = PedidoCompra
    template_name = "Detail/detail_pedido_convenio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle del Pedido compra'
        return context

class PapeleriaDetail(DetailView):
    model = PedidoPapeleria
    template_name = "Detail/detail_pedido_papeleria.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Pedido Papeleria'
        return context

class MensajesDetail(DetailView):
    model = Mensajes
    template_name = "Detail/detail_mensajes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Mensaje enviado'
        return context


#########################  PRINT ######################################################
#########################  PRINT ######################################################
#########################  PRINT ######################################################

class AvisaRetiroPrint(DetailView):
    model = AvisaRetiro
    template_name = "Detail/print_retira_cliente.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Avisa Retiro'
        return context





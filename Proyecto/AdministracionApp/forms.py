from django import forms

from .models import *
from FormulariosApp.models import PedidoCompra
from Proyecto.choices import estado_mercaderia, estado_pago
#############################################################

class MensajeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Mensajes
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control text-center","placeholder": 'Nombre', "type": 'text'}
            ),
            "asunto": forms.TextInput(
                attrs={"class": "form-control text-center","placeholder": 'Asunto', "type": 'text'}
            ),
            "mensaje": forms.Textarea(
                attrs={"class": "form-control text-center","placeholder": 'Mensaje', "rows":4}
            ),
        }
        exclude = ["usuario", "user_update", "respuesta"]

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data

class RegistroFraudeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistroFraudeForm,self).__init__(*args, **kwargs)
        self.fields['plataforma'].empty_label = "Plataforma"
        self.fields['forma_pago'].empty_label = "Forma de pago"
        self.fields['estado_mercaderia'].empty_label = "Estado mercaderia"
        self.fields['estado_pago'].empty_label = "Estado del pago"
        self.fields['fecha_venta'].label = "Fecha vta"
        self.fields["estado_mercaderia"].choices = [("", "Estado Mercaderia")]+list(self.fields["estado_mercaderia"].choices)[1:]
        self.fields["estado_pago"].choices = [("", "Estado Pago")]+list(self.fields["estado_pago"].choices)[1:]
        self.fields['liq_descuento'].label = "Fecha Liq Descontado"

    class Meta:
        model = RegistroFraudes
        fields = "__all__"
        widgets = {
            "plataforma": forms.Select(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Plataforma', "type": 'text'}
            ),
            "num_pedido": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Numero pedido', "type": 'number'}
            ),
            "fecha_venta": forms.DateInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Fecha venta', "type": 'date'}
            ),
            "forma_pago": forms.Select(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Forma de pago', "type": 'text'}
            ),
            "importe": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Importe', "type": 'number'}
            ),
            "ci_cliente": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Ci Cliente', "type": 'number'}
            ),
            "nombre_cliente": forms.TextInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Nombre Cliente', "type": 'text'}
            ),
            "num_factura": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Numero Factura', "type": 'number'}
            ),
            "num_nc": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Numero Nota Cred', "type": 'number'}
            ),
            "comentarios": forms.Textarea(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Comentarios', "type": 'text', "rows": 3}
            ),
            "estado_mercaderia": forms.Select(choices=estado_mercaderia,
                attrs={"class": "form-control text-center", "placeholder": 'Estado Mercaderia', "type": 'text'}
                                              ),
            "estado_pago": forms.Select(choices=estado_pago,
                attrs={"class": "form-control text-center",
                        "placeholder": 'Estado Pago', "type": 'text'}
                                        ),
            "liq_descuento": forms.DateInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Liquidacion donde descuenta', "type": 'date'}
            ),

        }
        exclude = ["usuario", "user_update", "estado", ]

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data

class RegistroFraudeEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistroFraudeEditForm,self).__init__(*args, **kwargs)
        self.fields['estado_pago'].empty_label = "Estado del pago"

    class Meta:
        model = RegistroFraudes
        fields = "__all__"
        widgets = {
            "estado_pago": forms.Select(choices=estado_pago,
                attrs={"class": "form-control text-center",
                        "placeholder": 'Estado Pago', "type": 'text'}
                                        ),
            "liq_descuento": forms.DateInput(
                attrs={"class": "form-control text-center",
                       "placeholder": 'Liquidacion donde descuenta', "type": 'date'}
            ),

        }
        exclude = ["usuario", "user_update", "estado", "estado_mercaderia", "comentarios", "num_nc", "num_factura",
                   "nombre_cliente", "ci_cliente", "importe", "forma_pago", "fecha_venta", "num_pedido", "plataforma", ]

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data



class PedidoCompraControlEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PedidoCompra
        fields = "__all__"
        widgets = {
            "control_adm": forms.CheckboxInput(
                attrs={
                    "class": "check-form","autofocus": "True"}
            ),
        }
        exclude = ["usuario", "user_update", "num_fun",
                   "cuotas", "importe", "nombre_fun", "ci_fun","importe_cuota","num_factura"]

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data


from django import forms
from .models import *
from Proyecto.choices import *

###########################################################################

class PedidoCompraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PedidoCompraForm, self).__init__(*args, **kwargs)
        self.fields["cuotas"].choices = [("", "Cuotas")]+list(self.fields["cuotas"].choices)[1:]
    class Meta:
        model = PedidoCompra
        fields = "__all__"
        widgets = {
            "num_fun": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "placeholder": "Numero del Funcionario", "autofocus": "True", "min": 1000, "max": 9999}
            ),
            "importe": forms.NumberInput(
                attrs={
                    "class": "form-control text-center", "placeholder": "Importe con descuento"}
            ),
            "cuotas": forms.Select(
                attrs={"class": "form-control text-center",
                            "placeholder": "Cuotas", "label": "Cuotas"}
                                   ),
        }
        exclude = ["usuario", "user_update", "num_factura","date_create","nombre_fun","ci_fun","importe_cuota","control_adm"]

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

class PedidoCompraEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PedidoCompra
        fields = "__all__"
        widgets = {
            "num_factura": forms.NumberInput(
                attrs={
                    "class": "form-control text-center", "placeholder": "Numero de factura", "autofocus": "True"}
            ),
        }
        exclude = ["usuario", "user_update", "num_fun",
                   "cuotas", "importe", "nombre_fun", "ci_fun","importe_cuota","control_adm"]

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


class PapeleriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PedidoPapeleria
        fields = "__all__"
        widgets = {
            "Lapiceras": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Lapiceras", "autofocus": "True"}
            ),
            "Clips": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Clips"}
            ),
            "Lapiz": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Lapiz"}
            ),
            "Grapas": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Grapas"}
            ),
            "ResmaA4": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Resma A4"}
            ),
            "Sobre_carta": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Sobre carta"}
            ),
            "Tijera": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Tijera"}
            ),
            "Banda_elastica": forms.NumberInput(
                attrs={"class": "form-control text-center",
                       "min": 0, "max": 10, "placeholder": "Banda elastica"}
            ),
            "Comentarios": forms.Textarea(
                attrs={"class": "form-control text-center",
                       "placeholder": "Comentarios", "rows": "4"}
            ),

        }
        exclude = ["usuario", "user_update", "Fecha_enviado"]

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


class AvisaRetiroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AvisaRetiroForm, self).__init__(*args, **kwargs)
        self.fields["suc_retirar"].empty_label = "Sucursal donde retira"


    class Meta:
        model = AvisaRetiro
        fields = "__all__"
        widgets = {
            "ci_cliente": forms.NumberInput(
                attrs={"class": "form-control text-center", "placeholder": "Cedula Cliente (Sin digito verificador)",
                       "min": 100000, "max": 9999999, "autofocus": "True"}
            ),
            "nombre_cliente": forms.TextInput(
                attrs={"class": "form-control text-center",
                       "placeholder": "Nombre Cliente"}
            ),
            "producto": forms.TextInput(
                attrs={"class": "form-control text-center", "placeholder": "Articulo",
                       "min_length": 17, "max_length": 17}
            ),
            "num_factura": forms.NumberInput(
                attrs={"class": "form-control text-center", "placeholder": "Numero Transaccion",
                       "min": 1, "max": 9999999}
            ),
            "suc_retirar": forms.Select(
                attrs={"class": "form-control text-center",
                       "placeholder": "Sucursal donde retira"}
            ),

        }
        exclude = ["usuario", "user_update", "fecha_retiro", "estado"]

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

class AvisaRetiroConfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = AvisaRetiro
        fields = "__all__"
        widgets = {
            "fecha_retiro": forms.DateInput(format='%d/%m/%Y',
                attrs={"class": "form-control text-center", "placeholder": "Fecha de entregado", "type": "date","label":"Fecha de entregado"}
            ),
        }
        exclude = ["usuario", "user_update",
                   "ci_cliente", "nombre_cliente", "producto","num_factura","suc_retirar", "estado"]

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

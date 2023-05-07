from django import forms
from .models import *
from datetime import datetime
from AdministracionApp.models import Comunicaciones
######################################################################################
today = datetime.today()


class ErroresForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ErroresForm,self).__init__(*args, **kwargs)
        self.fields['sucursal'].empty_label = "Sucursal"
        self.fields['grupo'].empty_label = "Grupo de error"
        self.fields['fecha_error'].label = "Fecha del Error"

    class Meta:
        model = Errores
        fields = "__all__"
        widgets = {
            "sucursal": forms.Select(
                attrs={"class": "form-control text-center", "type": 'text',
                    "autofocus": "True", "required": "True", 'placeholder': 'Sucursal'}
                ),
            "fecha_error": forms.DateInput(
                attrs={"class": "form-control  text-center", "type": 'date',  "required": "True",
                       'placeholder': 'Fecha error'}
            ),
            "num_cajera": forms.NumberInput(
                attrs={"class": "form-control  text-center", "type": 'number', 'min_length': 4,
                       'max_length': 4, "required": "True", 'placeholder': 'Num cajera'}
            ),
            "num_boleta": forms.NumberInput(
                attrs={"class": "form-control text-center", "type": 'number',
                       "required": "True", 'placeholder': 'Num boleta'}
            ),
            "grupo": forms.Select(
                attrs={"class": "form-control text-center", "type": 'text', "required": "True", 'placeholder': 'Grupo'}
            ),
            "comentario": forms.Textarea(
                attrs={"class": "form-control text-center", "type": 'text',
                       'rows': 3, 'placeholder': 'Comentarios'}
            ),
        }

        exclude = ["usuario", "user_update",]

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

class ManualesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Manuales
        fields = "__all__"
        widgets = {
            "nombre_manual": forms.TextInput(
                attrs={"class": "form-control text-center", "type": 'text',
                       "autofocus": "True", 'placeholder': 'Nombre manual'}
            ),
            "manual": forms.FileInput(
                attrs={"class": "form-control text-center", "type": 'file'}
            )
        }

        exclude = ["usuario", "user_update",]

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

class ComunicacionesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComunicacionesForm,self).__init__(*args, **kwargs)
        self.fields['medio_promo'].empty_label = "Forma de pago"

    class Meta:
        model = Comunicaciones
        fields = "__all__"
        widgets = {
            "medio_promo": forms.Select(
                attrs={"class": "form-control text-center", "type": 'text',
                       "autofocus": "True"}
            ),
            "valor_promo": forms.TextInput(
                attrs={"class": "form-control text-center", "type": 'text', 'placeholder':'Valor promo'}
            ),
            "descripcion_promo": forms.TextInput(
                attrs={"class": "form-control text-center", "type": 'text', 'placeholder':'Descripcion promo'}
            ),
            "imagen_promo": forms.FileInput(
                attrs={"class": "form-control text-center", "type": 'file', 'placeholder':'Imagen promo'}
            ),
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control text-center", "type": 'date'}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control text-center", "type": 'date'}
            ),

            "alcance_promo": forms.TextInput(
                attrs={"class": "form-control text-center", "type": 'text', 'placeholder':'Alcance'}
            ),
            "condiciones_promo": forms.Textarea(
                attrs={"class": "form-control text-center",
                       "type": 'text', "rows":3, "placeholder":"Condiciones"}
            ),
            "condiciones2_promo": forms.Textarea(
                attrs={"class": "form-control text-center", "type": 'text', "rows":3,"placeholder":"Condiciones"}
            ),
        }

        exclude = ["usuario", "user_update", "estado_promo"]

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

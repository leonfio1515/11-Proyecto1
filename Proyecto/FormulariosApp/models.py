from django.db import models
from django.conf import settings

from crum import get_current_user

from Proyecto.choices import *
from AdministracionApp.models import Sucursales
from FuncionariosApp.models import Funcionarios

from django.forms import model_to_dict
##################################################################################################################


class PedidoPapeleria(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_ped_papeleria", null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_ped_papeleria', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    cantidad_lapiceras = models.IntegerField(blank=True, null=True, name="Lapiceras")
    cantidad_clips = models.IntegerField(blank=True, null=True, name="Clips")
    cantidad_lapiz = models.IntegerField(blank=True, null=True, name="Lapiz")
    cantidad_grapas = models.IntegerField(blank=True, null=True, name="Grapas")
    cantidad_resmaA4 = models.IntegerField(blank=True, null=True, name="ResmaA4")
    cantidad_sobre_carta = models.IntegerField(blank=True, null=True, name="Sobre_carta")
    cantidad_tijera = models.IntegerField(blank=True, null=True, name="Tijera")
    cantidad_banda_elastica = models.IntegerField(blank=True, null=True, name="Banda_elastica")
    coment = models.CharField(max_length=200, name="Comentarios", blank=True, null=True)

    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")

    class Meta:
        verbose_name = "Pedido Papeleria"
        verbose_name_plural = "Pedido Papeleria"
        ordering = ["date_create"]

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(PedidoPapeleria, self).save()

class PedidoCompra(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_convenios", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_convenios', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    num_fun = models.ForeignKey(Funcionarios, on_delete=models.CASCADE, blank=True, null=True)
    nombre_fun = models.CharField(max_length=80, blank=True, null=True)
    ci_fun = models.IntegerField(blank=True, null=True)

    importe = models.IntegerField()
    cuotas = models.CharField(max_length=5, choices=cuotas)
    num_factura = models.PositiveIntegerField(blank=True, null=True)
    importe_cuota = models.FloatField()
    control_adm = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pedido Compra"
        verbose_name_plural = "Pedidos Compra"
        ordering = ["date_create"]

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(PedidoCompra, self).save()

class AvisaRetiro(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_retira_cliente", null=True, blank=True)
    date_create = models.DateField(auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_retira_cliente', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    ci_cliente = models.IntegerField()
    nombre_cliente = models.CharField(max_length=50)
    producto = models.CharField(max_length=17)
    num_factura = models.IntegerField()
    suc_retirar = models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    fecha_retiro = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Retira Cliente"
        verbose_name_plural = "Retira Cliente"
        ordering = ["date_create"]

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(AvisaRetiro, self).save()


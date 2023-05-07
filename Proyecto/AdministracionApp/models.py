from django.db import models
from django.conf import settings

from crum import get_current_user

from Proyecto.choices import *

from django.forms import model_to_dict
##########################################################################################################

class MediosPago(models.Model): #Se usa para los pagos de Venta Web (Financieras)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_medio_pago", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_medio_pago', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre_pago = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_pago

    class Meta:
        verbose_name = "Medios de Pago"
        verbose_name_plural = "Medios de Pago"

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
        super(MediosPago, self).save()


class Plataforma(models.Model): #Plataformas web de la empresa
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_plataforma", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_plataforma', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    plataforma = models.CharField(max_length=20)

    def __str__(self):
        return self.plataforma

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = "Plataformas"
        verbose_name_plural = "Plataformas"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Plataforma, self).save()

class MotivoDev(models.Model): #Motivos de devolucion de ventas web
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_motivo_dev", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_motivo_dev', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    motivoDevolucion = models.CharField(max_length=50)

    def __str__(self):
        return self.motivoDevolucion

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Motivo Dev"
        verbose_name_plural = "Motivo Dev"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(MotivoDev, self).save()

class Sucursales(models.Model): #Datos de sucursales
    user_create = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_sucursales", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_sucursales', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    numero_suc = models.CharField(max_length=3, blank=True, null=True)
    direccion_suc = models.CharField(max_length=60)
    departamento_suc = models.CharField(max_length=20, blank=True, null=True)
    zona_suc = models.CharField(max_length=90, blank=True, null=True)
    encargado_suc = models.CharField(max_length=90, blank=True, null=True)
    tel_suc = models.CharField(max_length=20, blank=True, null=True)
    cel_suc = models.CharField(max_length=20, blank=True, null=True)

    cod_amex = models.CharField(max_length=20, blank=True, null=True)
    cod_anda = models.IntegerField(blank=True, null=True)
    cod_cabal = models.CharField(max_length=20, blank=True, null=True)
    cod_club = models.IntegerField(blank=True, null=True)
    cod_creditel = models.IntegerField(blank=True, null=True)
    cod_creditosD = models.IntegerField(blank=True, null=True)
    cod_diners = models.IntegerField(blank=True, null=True)
    cod_lider = models.IntegerField(blank=True, null=True)
    cod_maestro = models.IntegerField(blank=True, null=True)
    cod_master = models.IntegerField(blank=True, null=True)
    cod_sodexo = models.IntegerField(blank=True, null=True)
    cod_oca = models.IntegerField(blank=True, null=True)
    cod_passcard = models.IntegerField(blank=True, null=True)
    cod_visa = models.IntegerField(blank=True, null=True)
    cod_tarjetad = models.IntegerField(blank=True, null=True)
    cod_edenred = models.CharField(max_length=20, blank=True, null=True)

    cod_retop = models.CharField(max_length=10, blank=True, null=True)
    user_retop = models.CharField(max_length=15, blank=True, null=True)
    pass_retop = models.CharField(max_length=20, blank=True, null=True)
    link_retop = models.CharField(max_length=500, blank=True, null=True)


    cod_pronto = models.CharField(max_length=5, blank=True, null=True)
    user_pronto = models.CharField(max_length=30, blank=True, null=True)
    pass_pronto = models.CharField(max_length=30, blank=True, null=True)
    link_pronto = models.CharField(max_length=500, blank=True, null=True)

    cod_inforcheck = models.CharField(max_length=5, blank=True, null=True)
    suc_inforcheck = models.CharField(max_length=5, blank=True, null=True)
    clave_inforcheck = models.CharField(max_length=10, blank=True, null=True)
    link_inforcheck = models.CharField(max_length=500, blank=True, null=True)

    user_taxfree = models.CharField(max_length=30, blank=True, null=True)
    pass_taxfree = models.CharField(max_length=30, blank=True, null=True)
    link_taxfree = models.CharField(max_length=500, blank=True, null=True)

    user_itau = models.CharField(max_length=30, blank=True, null=True)
    pass_itau = models.CharField(max_length=30, blank=True, null=True)
    link_itau = models.CharField(max_length=500, blank=True, null=True)

    fondo_fijo1 = models.PositiveIntegerField(blank=True, null=True)
    fondo_fijo2 = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.numero_suc

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ["numero_suc"]

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_create = user
            else:
                self.user_update = user
        super(Sucursales, self).save()


class Mensajes(models.Model): #Mensajes registrados desde las sucursales
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_mensaje", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_mensaje', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=2000)
    respuesta = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

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
        super(Mensajes, self).save()

class Comunicaciones(models.Model): #Comunicaciones activas para las sucursales
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_promocion", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_promocion', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    medio_promo = models.ForeignKey(MediosPago, on_delete=models.CASCADE)
    valor_promo = models.CharField(max_length=50)
    descripcion_promo = models.CharField(max_length=200)
    imagen_promo = models.ImageField(upload_to="media/", blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    alcance_promo = models.CharField(max_length=200)
    estado_promo = models.BooleanField(default=False)
    condiciones_promo = models.TextField(max_length=200, blank=True, null=True)
    condiciones2_promo = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Comunicacion"
        verbose_name_plural = "Comunicaciones"

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
        super(Comunicaciones, self).save()


class GrupoError(models.Model): #Grupos de errores de sucursales
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_grupoerror", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_grupoerror', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Grupo Error"
        verbose_name_plural = "Grupo Errores"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(GrupoError, self).save()

class CargoFuncionario(models.Model): #Cargos de funcionarios
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_cargofun", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_cargofun', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre_cargo = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_cargo

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Cargo Funcionario"
        verbose_name_plural = "Cargo Funcionarios"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(CargoFuncionario, self).save()



class RegistroFraudes(models.Model): #Fraudes
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_fraudes", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_fraudes', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    num_pedido = models.IntegerField(unique=True)
    fecha_venta = models.DateField()
    forma_pago = models.ForeignKey(MediosPago, on_delete=models.CASCADE)
    importe = models.IntegerField()

    ci_cliente = models.IntegerField()
    nombre_cliente = models.CharField(max_length=50)
    num_factura = models.IntegerField()
    num_nc = models.IntegerField()
    comentarios = models.CharField(max_length=200, blank=True, null=True)

    estado = models.CharField(max_length=10, default="Fraude")
    estado_mercaderia = models.CharField(
        max_length=20, choices=estado_mercaderia)
    estado_pago = models.CharField(max_length=20, choices=estado_pago)
    liq_descuento = models.DateField(blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Fraude"
        verbose_name_plural = "Fraudes"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(RegistroFraudes, self).save()

class Financieras(models.Model): #Info sobre las financieras (Arancel- plazos)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_financiera", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_financiera', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre_financiera = models.CharField(max_length=20)
    tel_contacto = models.CharField(max_length=20)
    email_contacto = models.CharField(max_length=200)
    web_financiera = models.CharField(max_length=500)
    usuario_finan = models.CharField(max_length=50, blank=True, null=True)
    contraseña_finan = models.CharField(max_length=20)
    rut = models.CharField(max_length=20, blank=True, null=True)
    medio_pago = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.nombre_financiera

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Financiera"
        verbose_name_plural = "Financieras"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Financieras, self).save()


class Area(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_area", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_area', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Area de la empresa"
        verbose_name_plural = "Areas de la empresa"

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Area, self).save()
   
from django.db import models
from django.conf import settings
from django.forms import model_to_dict

from crum import get_current_user

from AdministracionApp.models import Sucursales, GrupoError

######################################################################################

class Manuales(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_manual", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_manual', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre_manual = models.CharField(max_length=50)
    manual = models.FileField(upload_to="media/")

    class Meta:
        verbose_name = "Manuales"
        verbose_name_plural = "Manuales"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Manuales, self).save()


class Errores(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_errores", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_errores', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    sucursal= models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    fecha_error=models.DateField()
    num_cajera=models.IntegerField()
    num_boleta=models.IntegerField()
    grupo=models.ForeignKey(GrupoError, on_delete=models.CASCADE)
    comentario=models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Errores Cajeras"
        verbose_name_plural = "Errores Cajeras"

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
        super(Errores, self).save()

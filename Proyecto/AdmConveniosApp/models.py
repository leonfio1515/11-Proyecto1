from django.db import models
from django.conf import settings

from crum import get_current_user

############################################################################################
############################################################################################
############################################################################################

class HabilitaBoton(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_habilita_conv", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_habilita_conv', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre = models.CharField(max_length=20)
    boton = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Habilita boton"
        verbose_name_plural = "Habilita boton"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(HabilitaBoton, self).save()    
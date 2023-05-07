from django.db import models

from crum import get_current_user
from django.conf import settings

###############################################################################

class PreguntasFrec(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_preguntas_frec", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_preguntas_frec', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    nombre = models.CharField(max_length=50)
    pregunta = models.TextField(max_length=300)
    respuesta = models.TextField(max_length=500)
    image = models.ImageField(upload_to='pregfrec/%Y/%m/%d', null=True, blank=True)


    class Meta:
        verbose_name = "Preguntas frecuentes"
        verbose_name_plural = "Preguntas frecuentes"
        ordering = ["date_create"]

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(PreguntasFrec, self).save()


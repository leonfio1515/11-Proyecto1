from django.db import models
from django.conf import settings
from crum import get_current_user

from Proyecto.choices import sexo, estado_funcionario
from AdministracionApp.models import CargoFuncionario, Sucursales

##############################################################################################

class Funcionarios(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_create_funcionarios", null=True, blank=True)
    date_create = models.DateField(
        auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update_funcionarios', null=True, blank=True)
    date_update = models.DateField(auto_now=True, null=True, blank=True)

    numero_funcionario = models.IntegerField(unique=True, primary_key=True)

    cedula_funcionario=models.IntegerField()
    nombre_funcionario=models.CharField(max_length=30)
    apellido_funcionario=models.CharField(max_length=30)
    cargo_funcionario = models.ForeignKey(CargoFuncionario, on_delete=models.CASCADE)
    sexo_funcionario = models.CharField(max_length=30, choices=sexo)
    fecha_ingreso=models.DateField()
    estado_funcionario=models.CharField(max_length=30, choices=estado_funcionario)
    limite_saldo = models.IntegerField(default=2500, blank=True, null=True)
    disponible_funcionario = models.FloatField(default=0, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.numero_funcionario)

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario = user
            else:
                self.user_update = user
        super(Funcionarios, self).save()


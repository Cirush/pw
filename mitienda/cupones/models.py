from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Cupon(models.Model):
    codigo = models.CharField(max_length = 50, unique = True)
    valido_desde = models.DateTimeField()
    valido_hasta = models.DateTimeField()
    descuento = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    activo = models.BooleanField()

    class Meta:
        verbose_name_plural = "Cupones"
    def __str__(self):
        return self.codigo

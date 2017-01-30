from __future__ import unicode_literals

from django.db import models
from tienda.models import Producto

# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    email = models.EmailField()
    direccion = models.CharField(max_length = 250)
    codigo_postal = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 100)
    creado = models.DateTimeField(auto_now_add = True)
    actualizado = models.DateTimeField(auto_now = True)
    pagado = models.BooleanField(default = False)

    class Meta:
        ordering = ('-creado',)

    def __str__(self):
        return 'Pedido {}'.format(self.id)

    def get_coste_total(self):
        return sum(item.get_coste() for item in self.items.all())

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name = 'items')
    producto = models.ForeignKey(Producto, related_name = 'pedido_items')
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    cantidad = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_coste(self):
        return self.precio * self.cantidad

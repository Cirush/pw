from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length = 200, db_index = True)
	slug = models.SlugField(max_length = 200, db_index = True, unique = True)

	class Meta:
		ordering = ("nombre",)
		verbose_name = "categoria"
		verbose_name_plural = "categorias"

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
	    return reverse("tienda:producto_listado_por_categoria", args=[self.slug])


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name = "productos")
    nombre = models.CharField(max_length = 200, db_index = True)
    slug = models.SlugField(max_length = 200, db_index = True)
    imagen = models.ImageField(upload_to ='productos',blank = True)
    descripcion = models.TextField(blank = True)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default = True)
    creado = models.DateTimeField(auto_now_add = True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)
        index_together = (("id", "slug"),)
    def get_absolute_url(self):
	return reverse('tienda:detalle_producto', args=[self.id, self.slug])
    def __str__(self):
        return self.nombre



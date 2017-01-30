from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "slug"]
    prepopulated_fields = {"slug":("nombre",)}
admin.site.register(Categoria,CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "slug", "precio", "stock", "disponible", "creado", "actualizado"]
    list_filter = ["disponible", "creado", "actualizado"]
    list_editable = ["precio", "stock", "disponible"]
    prepopulated_fields = {"slug": ("nombre",)}
admin.site.register(Producto,ProductoAdmin)

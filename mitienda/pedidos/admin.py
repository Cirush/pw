from django.contrib import admin
from .models import Pedido, PedidoItem
# Register your models here.

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    raw_id_fields = ['producto']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellidos", "email", "direccion", "codigo_postal", "ciudad", "pagado", "creado", "actualizado"]
    list_filter = ["pagado", "creado", "actualizado"]
    inlines = [PedidoItemInline]

admin.site.register(Pedido, PedidoAdmin)

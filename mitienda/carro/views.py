from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from tienda.models import Producto
from .carro import Carro
from .forms import CartAddProductForm
from cupones.forms import CouponApplyForm
# Create your views here.
@require_POST
def agregar_a_carro(request, id_producto):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=id_producto)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carro.add(producto=producto, cantidad = cd['cantidad'],actualizar_cantidad = cd['actualizar'])
    return redirect('carro:detalle_carro')

def eliminar_de_carro(request, id_producto):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id = id_producto)
    carro.remove(producto)
    return redirect("carro:detalle_carro")

def detalle_carro(request):
    carro = Carro(request)
    for item in carro:
        item["update_quantity_form"] = CartAddProductForm(initial={'cantidad':item['cantidad'],'actualizar': True})
    coupon_apply_form = CouponApplyForm()
    return render(request, 'carro/detalle.html', {'carro':carro,'coupon_apply_form':coupon_apply_form})

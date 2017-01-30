from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from carro.forms import CartAddProductForm
# Create your views here.

def listar_producto(request, category_slug = None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible = True)
    if category_slug:
        categoria = get_object_or_404(Categoria, slug = category_slug)
        productos = productos.filter(categoria = categoria)
    return render(request, "tienda/producto/lista.html", {"categoria":categoria, "categorias":categorias,"productos":productos})

def detalle_producto(request, id, slug):
    producto = get_object_or_404(Producto, id = id, slug = slug, disponible = True)
    cart_product_form = CartAddProductForm()
    return render(request, "tienda/producto/detalle.html",{"producto":producto, 'cart_product_form':cart_product_form})

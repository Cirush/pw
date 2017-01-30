from django.shortcuts import render
from .models import PedidoItem
from .forms import OrderCreateForm
from carro.carro import Carro
# Create your views here.

def crear_pedido(request):
    carro = Carro(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            for item in carro:
                PedidoItem.objects.create(pedido=pedido, producto=item["producto"], precio =item["precio"],cantidad = item["cantidad"])

            #borrar carrito
            carro.clear()
        return render(request, "pedidos/pedido/creado.html",{"pedido":pedido})
    else:
        form = OrderCreateForm()
    return render(request, "pedidos/pedido/crear.html", {"carro":carro, "form":form})

from decimal import Decimal
from django.conf import settings
from tienda.models import Producto
from cupones.models import Cupon

class Carro(object):

    def __init__(self,request):
        """
            Inicializar el carrito.
        """
        self.session = request.session
        carro = self.session.get(settings.CART_SESSION_ID)
        if not carro:
            #guardar un carrito vacio en la sesion.
            carro = self.session[settings.CART_SESSION_ID] = {}
        self.carro = carro
        #guardar el cupon aplicado
        self.cupon_id = self.session.get('cupon_id')

    def __len__(self):
        """
        Cuenta los items en el carrito
        """
        return sum(item['cantidad'] for item in self.carro.values())

    def __iter__(self):
        """
        Itera sobre los items del carrito y obtiene los productos de la base de datos
        """
        ids_productos = self.carro.keys()
        #obtiene los objetos producto y los agrega al carro
        productos = Producto.objects.filter(id__in=ids_productos)
        for producto in productos:
            self.carro[str(producto.id)]['producto'] = producto

        for item in self.carro.values():
            item['precio']=Decimal(item['precio'])
            item['precio_total'] = item['precio']*item['cantidad']
            yield item

    def add(self, producto, cantidad = 1, actualizar_cantidad = False):
        """
        Agregar un producto al carrito o actualizar su cantidad.
        """
        id_producto = str(producto.id)
        if id_producto not in self.carro:
            self.carro[id_producto] = {"cantidad":0,"precio":str(producto.precio)}
        if actualizar_cantidad:
            self.carro[id_producto]["cantidad"]= cantidad
        else:
            self.carro[id_producto]["cantidad"] += cantidad
        self.save()

    def remove(self,producto):
        """
        Elimina un producto del carro.
        """
        id_producto = str(producto.id)
        if id_producto in self.carro:
            del self.carro[id_producto]
            self.save()


    def save(self):
        #actualizar el carrito de sesion
        self.session[settings.CART_SESSION_ID] = self.carro
        #marcar la sesion como modificada para asegurar que se guardar
        self.session.modified = True

    def clear(self):
        #elimina el carro de la sesion
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True




    def get_precio_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())



    @property
    def cupon(self):
        if self.cupon_id:
            return Cupon.objects.get(id = self.cupon_id)
            return None

    def get_descuento(self):
        if self.cupon:
            return(self.cupon.descuento / Decimal('100')) * self.get_precio_total()
        return Decimal('0')

    def get_precio_total_descontado(self):
        return self.get_precio_total() - self.get_descuento()

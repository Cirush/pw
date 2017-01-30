from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.detalle_carro, name = 'detalle_carro'),
    url(r'^agregar/(?P<id_producto>\d+)/$', views.agregar_a_carro, name = 'agregar_a_carro'),
    url(r'^eliminar/(?P<id_producto>\d+)/$', views.eliminar_de_carro, name = 'eliminar_de_carro'),

]

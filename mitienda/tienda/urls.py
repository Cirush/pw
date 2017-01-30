from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listar_producto, name = "listar_producto"),
    url(r'^(?P<category_slug>[-\w]+)/$',views.listar_producto, name = "producto_listado_por_categoria"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detalle_producto, name="detalle_producto"),
]

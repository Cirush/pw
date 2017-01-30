from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^crear/$', views.crear_pedido, name = 'crear_pedido'),
]

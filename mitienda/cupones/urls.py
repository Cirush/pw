from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^aplicar/$', views.aplicar_cupon, name = 'aplicar'),
]

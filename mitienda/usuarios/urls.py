from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^registro/$', registroUsuario, name = 'registro' ),
    url(r'^perfil/$', editarUsuario, name = 'perfil'),
    url(r'^login/$', usuarioLogin, name = 'login'),
    url(r'^logout/$', usuarioLogout, name = "logout"),
]

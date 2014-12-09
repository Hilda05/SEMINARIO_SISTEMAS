from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto_juego.apps.inicio.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'proyecto_juego.apps.inicio.views.home', name='hola'),
    url(r'^hola$', 'proyecto_juego.apps.inicio.views.home', name='hola1'),

    #url(r'^$', 'proyecto_juego.apps.inicio.views.registro', name='registro'),
    #url(r'^$', 'proyecto_juego.apps.inicio.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/$','proyecto_juego.apps.inicio.views.registro_usuarios', name='registro_usuarios'),
    url(r'^registrar/$','proyecto_juego.apps.inicio.views.registrou', name='registrou'),
    url(r'^ingresar/$','proyecto_juego.apps.inicio.views.ingresar', name='ingresar'),
    
)

#http://localhost:8000/
from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto_juego.apps.inicio.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'proyecto_juego.apps.inicio.views.home', name='hola'),

    

    url(r'^admin/', include(admin.site.urls)),
)

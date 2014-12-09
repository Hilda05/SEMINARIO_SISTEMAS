from django.conf.urls import patterns, include, url
from .views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'juego.apps.comienso.views.home', name='home'),

    url(r'^home$', 'juego.apps.comienso.views.home', name='home1'),

    
    url(r'^registrar/$','juego.apps.comienso.views.registrou', name='registrou'),
    url(r'^ingresar/$','juego.apps.comienso.views.ingresar', name='ingresar'),
    url(r'^perfil/$',perfil),
    url(r'^active/$',user_active_view),
    url(r'^logout/$',logout_view),
    url(r'^lista/$',listar),
    url(r'^modificar/$',modificar_view),
    url(r'^npass/$',modificar_pass),
    url(r'^perfil/view/(\d+)/$',ver_perfil, name='ver_perfil_user'),
    url(r'^permit/$', error_permisos),


    url(r'^tema/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
    url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
    #url(r'^agregar/',agregar, name='agregar_pregunta'),

    #================================

    url(r'^chat/$',chat, name='coneccion'),



)

#http://localhost:8000/

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('juego.apps.comienso.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
)

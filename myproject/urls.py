from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from filebrowser.sites import site
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rostermaker.models import Player

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mprsoftball.views.home', name='home'),
    # url(r'^mprsoftball/', include('mprsoftball.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'views.main', name='main'),
    url(r'^players/', 'rostermaker.views.players', name="players_list"),
)

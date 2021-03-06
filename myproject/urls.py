from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from filebrowser.sites import site
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rostermaker.models import Player

from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()

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
    url(r'^current/', 'gamemaker.views.current',),
    url(r'^season/', 'season.views.prior'),
    url(r'^hall/', 'rostermaker.views.hall_main'),
    url(r'^photos/', 'photo.views.gallery_main'),
    url(r'^season_detail/(?P<season>\d{4})/$', 'season.views.season_detail'),
    url(r'^stats/','gamemaker.views.stats',),
    url(r'^current/','gamemaker.views.leaders',),
    url(r'^directions', 'views.directions', name='directions'),
    url(r'^player_detail/(?P<player_id>\d+)/$', 'rostermaker.views.player_detail'),
    url(r'^random_pics','photo.views.random_pics'),
    url(r'^season_quicklink','season.views.season_quicklink'),
    url(r'^player_quicklink','season.views.player_quicklink'),
    url(r'^priorlinks','season.views.priorlinks'),
)

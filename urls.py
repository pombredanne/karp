from django.conf.urls import patterns, include, url

from django.contrib import admin
from karp.views import IndexView
from apps.comparison import urls as comparison_url
from apps.statictext import urls as statictext_url
from apps.rsi import urls as rsi_url

admin.autodiscover()

urlpatterns = patterns('',
                       url('^$', IndexView.as_view(), name="home"),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include(statictext_url)),
                       url(r'^', include(comparison_url)),
                       url(r'^', include(rsi_url)),
                       )

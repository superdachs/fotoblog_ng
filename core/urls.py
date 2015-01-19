from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
  url(r'^$', 'core.views.site', name='category'),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from category.models import Category_Instance

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fotoblog_ng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'core.views.index', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<category>\w+)/$', include('core.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

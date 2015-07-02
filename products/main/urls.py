from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalog.urls')),
    url(r'^swagger/', include('rest_framework_swagger.urls')),
    url(r'^user/', include('user_app.urls')),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[ 1: ], serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[ 1: ],
        'django.contrib.staticfiles.views.serve', dict(insecure=True)),

]

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalog.urls')),
    url(r'^swagger/', include('rest_framework_swagger.urls')),
    url(r'^user/', include('user_app.urls')),

]

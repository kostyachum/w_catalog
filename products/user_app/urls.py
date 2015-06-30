from django.conf.urls import url
from user_app import views
from django.conf import settings


urlpatterns = [
	url(r'^authapi/', views.AuthenticationApi.as_view(), name='authapi'),
]

from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


class SerialUser(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['pk', 'username', 'password']	
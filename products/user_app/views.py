from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, serializers
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from user_app.serializers import SerialUser

class AuthenticationApi(APIView):
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	serializer_class = SerialUser

	def post(self, request, *args, **kwargs):
	
		user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
		login(request, user)
		return HttpResponseRedirect('/')

	def delete(self, request, *args, **kwargs):
		"""Logout from system"""
		
		logout(request)
		return Response("ok")


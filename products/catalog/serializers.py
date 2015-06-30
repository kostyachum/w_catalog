from rest_framework import routers, serializers, viewsets
from catalog.models import Category, Product


class SerialCategory(serializers.ModelSerializer):

	class Meta:

		model = Category
		fields = ['pk', 'name', 'parent']

class SerialProductForAdd(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ['pk','name', 'description', 'category', 'price']	

class SerialProduct(serializers.ModelSerializer):

	category = serializers.ReadOnlyField(source='category_name')

	class Meta:
		model = Product
		fields = ['pk','name', 'description', 'category', 'price']
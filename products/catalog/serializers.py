from rest_framework import routers, serializers, viewsets
from catalog.models import Category, Product


class SerialCategory(serializers.ModelSerializer):

	class Meta:

		model = Category
		fields = ['pk', 'name', 'parent']

class SerialProductForAdd(serializers.ModelSerializer):
	url = serializers.URLField(read_only=True)

	class Meta:
		model = Product
		fields = ['pk','name', 'description', 'category', 'price', 'image_url', 'url']	

class SerialProduct(serializers.HyperlinkedModelSerializer):
	category = serializers.ReadOnlyField(source='category_name')

	class Meta:
		model = Product
		fields = ['pk', 'name', 'category', 'price', 'image_url', 'url']


class SerialProductDetail(serializers.ModelSerializer):
	category = serializers.ReadOnlyField(source='category__name')

	class Meta:
		model = Product
		fields = ['pk','name', 'description', 'category', 'price', 'image_url']

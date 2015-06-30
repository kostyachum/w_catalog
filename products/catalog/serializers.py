from rest_framework import routers, serializers, viewsets
from catalog.models import Category, Product


class SerialCategory(serializers.ModelSerializer):

	class Meta:

		model = Category
		fields = ['pk', 'name', 'parent']

class SerialProductForAdd(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ['pk','name', 'description', 'category', 'price', 'image_url']	

class SerialProduct(serializers.ModelSerializer):

	category = serializers.ReadOnlyField(source='category_name')
	#url = serializers.HyperlinkedRelatedField(many=True, view_name='product_detail', read_only=True)
	#url = GiveAbsolute(source="product_detail")

	class Meta:
		model = Product
		fields = ('pk','name', 'category', 'price', 'image_url')

class SerialProductDetail(serializers.ModelSerializer):

	category = serializers.ReadOnlyField(source='category_name')

	class Meta:
		model = Product
		fields = ['pk','name', 'description', 'category', 'price', 'image_url']


from django.shortcuts import render
from catalog.models import Category, Product
from catalog.serializers import SerialProduct, SerialProductForAdd, SerialCategory  
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status, serializers, generics
from rest_framework.response import Response
import django_filters
from rest_framework import filters
import mptt


class ProductFilter(django_filters.FilterSet):

	price = django_filters.NumberFilter(name="price")
	category = django_filters.CharFilter(name="category__name", lookup_type='contains')

	class Meta:
		model = Product
		fields = ['category', "price"]


class ProductList(generics.ListAPIView):
	"""
	Product search

	?category=horror&price=200
	?ordering=-price	
	"""
	queryset = Product.objects.all()
	serializer_class = SerialProduct
	filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
	permission_classes = (permissions.IsAuthenticated,)
	filter_class = ProductFilter
	ordering_fields = ('price')


class ProductViewSet(viewsets.ModelViewSet):
	"""
	Get list of products
	Add, edit, delete
	"""

	queryset = Product.objects.all()
	serializer_class = SerialProductForAdd
	permission_classes = (permissions.IsAuthenticated,)

	def list(self, request):
		queryset = Product.objects.all()
		serializer = SerialProduct(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		serializer = SerialProductForAdd(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		queryset = Category.objects.all()
		get_categ = get_object_or_404(queryset, pk=pk)
		serializer = SerialProduct(get_categ)
		return Response(serializer.data)


class CategoryViewFilter(viewsets.ModelViewSet):
	"""
	Category search

	name/horror	
	"""
	def filter(self, request, *args, **kwargs):
		""" Returns  list by category"""

		name = kwargs['name']
		category = Category.objects.get(name=name)
		children = category.get_descendants()
		serializer = SerialCategory(children, many=True)
		return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
	"""
	Returns a list of  categories. 
	Add, edit, delete
	"""

	queryset = Category.objects.all()
	serializer_class = SerialCategory
	permission_classes = (permissions.IsAuthenticated,)

	def create(self, request):
		serializer = SerialCategory(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		queryset = Category.objects.all()
		get_categ = get_object_or_404(queryset, pk=pk)
		serializer = SerialCategory(get_categ)
		return Response(serializer.data)	



from django.shortcuts import render
from catalog.models import Category, Product
from catalog.serializers import SerialProduct, SerialProductDetail, SerialProductForAdd, SerialCategory  
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status, serializers, generics, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse, reverse_lazy
import django_filters
from rest_framework import filters
import mptt
from catalog.mycache import ProductDetailJob, CategoryListJob
from catalog.signals import invalidate_product, invalidate_category

from django.views.generic import TemplateView


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

	def create(self, request, *args, **kwargs):
		cat = Category.objects.get(id=request.data['category'])
		serializer = Product(name=request.data['name'], 
							description=request.data['description'], 
							category=cat, 
							price=request.data['price'],
					)
		serializer.save()
		serializer.url = reverse_lazy('product_detail', request=request, kwargs={'pk': serializer.pk})
		serializer.save()
		return Response(status=status.HTTP_201_CREATED)

	def retrieve(self, request, pk=None):
		try:
			queryset = ProductDetailJob().get(pk=unicode(pk))
			serializer = SerialProductDetail(queryset, many=False)
		except Product.DoesNotExist:
			return Response("no product")
		return Response(serializer.data)

		
class CategoryViewFilter(viewsets.ModelViewSet):
	"""
	Category search

	/1/	
	"""
	serializer_class = SerialCategory
	def filter(self, request, *args, **kwargs):
		""" Returns  list by category"""
		print 
		pk = kwargs['pk']
		category = Category.objects.get(pk=pk)
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
	
	def list(self, request):
		queryset = CategoryListJob().get()
		serializer = SerialCategory(queryset, many=True)
		return Response(serializer.data)	

	def create(self, request):
		serializer = SerialCategory(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		try:
			queryset = Category.objects.get(pk=pk)
			serializer = SerialCategory(queryset, many=False)
		except Category.DoesNotExist:
			return Response("no category like it")
		return Response(serializer.data)	


class ProductView(TemplateView):
	def get_context_data(self, **kwargs):
		context = super(ProductView, self).get_context_data(**kwargs)
		# update the context
		return context
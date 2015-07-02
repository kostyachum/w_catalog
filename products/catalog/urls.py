from django.conf.urls import url
from catalog import views
from django.conf import settings


list_category = views.CategoryViewSet.as_view({
	'get': 'list',
	'post':'create'
	})

category_detail = views.CategoryViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
	})

list_product = views.ProductViewSet.as_view({
	'get': 'list',
	'post':'create'
	})

product_detail = views.ProductViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
	})

filter_category = views.CategoryViewFilter.as_view({
	'get': 'filter',	
})

urlpatterns = [
	url(r'^$', list_product, name="main"),
	url(r'^products/$', list_product, name="main"),
	url(r'^products/(?P<pk>\d+)/$', product_detail, name="product_detail"),
	url(r'^category/$', list_category),
	url(r'^category/(?P<pk>\d+)/$', category_detail),
	url(r'^products/search/$', views.ProductList.as_view()),
	url(r'^category/search/(?P<pk>[0-9a-zA-Z_-]+)/$',filter_category),
    url(r'^main/', views.ProductView.as_view(template_name='catalog/index.html'), name='main'),

]

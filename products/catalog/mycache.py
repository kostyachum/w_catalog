from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from cacheback.base import Job
from catalog.models import Product, Category

class ProductDetailJob(Job):
	lifetime = 60*100
	fetch_on_miss = False

	def fetch(self, pk):
		return Product.objects.get(pk=pk)

class CategoryListJob(Job):
	lifetime = 60*100
	fetch_on_miss = False

	def fetch(self):
		return Category.objects.all()

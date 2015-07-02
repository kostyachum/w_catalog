from cacheback.base import Job
from catalog.models import Product, Category


class ProductDetailJob(Job):
	lifetime = 60*100
	fetch_on_miss = True

	def fetch(self, *args, **kwargs):
		try: 
			queryset = Product.objects.prefetch_related('category__parent').get(pk=kwargs['pk'])
		except Exception:
			return "no product"
		return queryset

class CategoryListJob(Job):
	lifetime = 60*100
	fetch_on_miss = True

	def fetch(self):
		return Category.objects.all()


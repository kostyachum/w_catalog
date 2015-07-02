from catalog.models import Category, Product
from catalog.mycache import ProductDetailJob, CategoryListJob
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

invalidate_signals = [post_delete, post_save]

@receiver(invalidate_signals, sender=Product)
def invalidate_product(sender, instance, **kwargs):
	print "Invalidate product", kwargs
	ProductDetailJob().invalidate(pk=unicode(instance.pk))

@receiver(invalidate_signals, sender=Category)
def invalidate_category(sender, instance, **kwargs):
	CategoryListJob().invalidate()
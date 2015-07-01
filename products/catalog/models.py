from django.db import models
from mptt.models import MPTTModel
import mptt
from django .contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Category(models.Model):
	name = models.CharField(max_length=100)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

	def __unicode__(self):
		return self.name

	def all_children(self):
		return self.name.get_descendants()

mptt.register(Category,)

class Product(models.Model):

	name = models.CharField(max_length=120)
	description = models.TextField()
	category = models.ForeignKey(Category)
	price = models.DecimalField(max_digits=19, decimal_places=2)
	image_url = models.ImageField(upload_to='images/product_image', blank=True, null=True)
	url = models.URLField()

	def __unicode__(self):		
		return '{0} - {1}'.format(self.pk, self.name)

	def category_family(self):	
		return self.category.get_family().values()

# @receiver(post_save, sender=Product)
# def on_change(instance, **kwargs):
# 	#cache.set('product::%(id)d' % {'id': instance.id}, instance)
# 	print "wwwwww"
# 	job = Product()
# 	job.invalidate(name)

# @receiver(post_delete, sender=Product)
# def on_delete(instance, **kwargs):
# 	#cache.delete('product::%(id)d' % {'id': instance.id})
# 	print "qqq"
# 	job = Product()
# 	job.delete(name)

from django.db import models
from .utils import code_generator, create_shortcode


class KirrURLManager(models.Manager):
	def all(self,*args, **kwargs):
		qs_main = super(KirrURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=100):
		qs = KirrURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1 
		return "new codes made: {i}".format(i=new_codes)

# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220,)
	shortcode = models.CharField(max_length=15, unique=True,  blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	objects = KirrURLManager()
	some_random = KirrURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or  self.shortcode == "" :
			self.shortcode = code_generator()
		super(KirrURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)
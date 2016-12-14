from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
	help = "Refreshed all KirrURL shortcodes"


	def add_arguments(seld, parser):
		#argumentos para pasar en el coomand line
		parser.add_argument("items", type=int)

	def handle(self, *args, **options):  
		return KirrURL.objects.refresh_shortcodes(items=options['items'])

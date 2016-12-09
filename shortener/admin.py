from django.contrib import admin

# Register your models here.
from .models import KirrURL

@admin.register(KirrURL)
class KirrURLAdmin(admin.ModelAdmin):
	pass
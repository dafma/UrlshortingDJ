from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm


def test_view(request):
	return HttpResponse("some stuff")


# Create your views here.
def kirr_redirect_view(request, shortcode=None,*args, **kwargs):
	"""
	print(args)
	print(kwargs)
	obj = KirrURL.objects.get(shortcode=shortcode)
	try:
		obj = KirrURL.objects.get(shortcode=shortcode)
	except:
		obj = KirrURL.objects.all().first()
	"""
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	obj_url = obj.url

	# obj_url = None	
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url
	return HttpResponseRedirect(obj.url)


class KirrRedirectView(View):
	def get(self, request, shortcode=None,*args, **kwargs):
		print(args)
		print(kwargs)
		return HttpResponse("Hello  {sc}".format(sc=shortcode))





class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Submit Url",
			"form":the_form,
		}
		return render(request, 'home.html', context)

	def post(self, request, *args, **kwargs):
		some_dict = {}
		#some_dict['url'] error
		#some_dict.get('url')
		#print(request.POST["url"])
		
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
		context = {
			"form":form
		}
		return render(request, 'home.html', context)
		


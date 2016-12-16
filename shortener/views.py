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



class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        
        return HttpResponseRedirect(obj.url)



class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		bg_image = 'https://upload.wikimedia.org/wikipedia/commons/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg'
		context = {
            "title": "Kirr.co",
            "form": the_form,
            "bg_image": bg_image
        }
		return render(request, "home.html", context) # Try Django 1.8 & 1.9 http://joincfe.com/youtube
	
	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
	            "title": "Kirr.co",
	            "form": form
	    }
		template = "home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
	                "object": obj,
	                "created": created,
	        }
			if created:
				template = "success.html"
			else:
				template = "already-exists.html"
		return render(request, template ,context)


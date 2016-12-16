from django.conf.urls import url
from django.contrib import admin
from shortener.views import KirrRedirectView, kirr_redirect_view, test_view, HomeView
from shortener import views

#no hacer esto
#from shortener import views
#from another_app.views import views


urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    #url(r'^(?P<shortcode>[\w-]+){6, 15}$', kirr_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+){6, 15}$', KirrRedirectView.as_view()),
]

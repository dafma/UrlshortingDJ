from django.conf import settings
from django_hosts import patterns, host

host_patterns =  patterns('',
	host(r'www', settings.ROOT_URLCONF, name='www'),
	host(r'live', settings.ROOT_URLCONF, name='live'),
	host(r'(?!www).*', 'UrlshortingDJ.hostsconf.urls', name='willcard'),
)

"""
from UrlshortingDJ.host import urls as redirect_urls
host_patterns =  patterns(''
	host(r'www', settings.ROOT_URLCONF, name='www'),
	host(r'(?!www).*', redirect_urls, name='willcard'),
)
"""
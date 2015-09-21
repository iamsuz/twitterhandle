# from django.conf.urls import include, url
from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     url(r'^$', 'twitter.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     # url(r'^admin/', include(admin.site.urls)),
# ]
from django.conf.urls import patterns, include, url
from twitter.views import *

urlpatterns = patterns('',
    url(r'^search/', home),
    # url(r'^index/', index),
    url(r'^admin/', include(admin.site.urls)),
)
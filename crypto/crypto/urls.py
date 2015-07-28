from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crypto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^safe_message/', 'tutorial.views.safe_message', name="safe_message"),
    url(r'^message/', 'tutorial.views.message', name="message"),
    url(r'^test/', 'tutorial.views.test', name="test")


)

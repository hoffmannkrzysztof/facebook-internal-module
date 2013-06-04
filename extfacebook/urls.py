from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login$', 'extfacebook.views.login', name="fb_login"),
                       url(r'^callback', 'extfacebook.views.callback', name="fb_callback"),
)

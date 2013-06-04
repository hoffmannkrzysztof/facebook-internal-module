import urllib
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def login(request):

    internal_redirect = request.GET.get('internal_redirect', '/')

    args_internal = {
        'internal_redirect': request.build_absolute_uri( internal_redirect )
    }

    args = {
        'client_id': request.website.app_id,
        'scope': 'email,publish_actions,read_stream,manage_pages,user_online_presence,user_birthday,user_likes,user_location',
        'redirect_uri': request.build_absolute_uri(reverse('fb_callback'))+"?"+urllib.urlencode(args_internal),
    }

    return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))


def callback(request):
    code = request.GET.get('code', None)
    user = authenticate(token=code, request=request)
    django_login(request, user)
    request.user = user

    return HttpResponseRedirect(request.GET['internal_redirect'])




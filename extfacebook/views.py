# coding=utf-8

import urllib
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from extfacebook.settings import FACEBOOK_AUTH_PERMISSION


def login(request):

    internal_redirect = request.GET.get('internal_redirect', request.GET.get('next', '/'))

    args_internal = {
        'internal_redirect': request.build_absolute_uri( internal_redirect )
    }

    args = {
        'client_id': request.website.app_id,
        'scope': ",".join(FACEBOOK_AUTH_PERMISSION),
        'redirect_uri': request.build_absolute_uri(reverse('fb_callback'))+"?"+urllib.urlencode(args_internal),
    }

    return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))


def callback(request):
    if request.GET.get('error',None) is not None:
        messages.error(request,u'Wystąpił błąd podczas autoryzacji lub rejestracja została anulowana. Spróbuj ponownie.')
        return HttpResponseRedirect(request.GET.get('internal_redirect', '/'))

    if 'facebook' in request.META['HTTP_USER_AGENT'] or 'Google' in request.META['HTTP_USER_AGENT']:
        return HttpResponseRedirect(request.GET.get('internal_redirect', '/'))

    code = request.GET.get('code', None)
    user = authenticate(token=code, request=request)
    django_login(request, user)
    request.user = user
    messages.success(request,u'Dziękujemy! Zostałeś zalogowany.')

    return HttpResponseRedirect(request.GET.get('internal_redirect', '/'))




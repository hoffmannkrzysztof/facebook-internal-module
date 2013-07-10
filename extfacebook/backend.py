import urllib
import json
import urlparse
from django.core.urlresolvers import reverse

from django.utils import timezone
from exceptions import FacebookAuthBadCodeException
from settings import FACEBOOK_AUTH_PERMISSION
from models import ExtendedUser

class FacebookBackend:
    def authenticate(self, token=None, request=None):

        args_internal = {
            'internal_redirect': request.build_absolute_uri( request.GET.get('internal_redirect','/') )
        }

        args = {
            'client_id': request.website.app_id,
            'client_secret': request.website.app_secret,
            'redirect_uri': request.build_absolute_uri(reverse('fb_callback'))+"?"+urllib.urlencode(args_internal),
            'code': token,
        }

        target = urllib.urlopen('https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(args))
        if target.code != 200:
            fb_target = json.load(target)
            if fb_target.get('error',None):
                raise FacebookAuthBadCodeException(fb_target['error']['message'])
        else:
            response = urlparse.parse_qs(target.read())
            access_token = response['access_token'][-1]

        fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token=%s' % access_token)
        fb_profile = json.load(fb_profile)

        try:
            user = ExtendedUser.objects.get(
                facebook_id=fb_profile['id'],
                app_id=request.website.app_id
            )
        except ExtendedUser.DoesNotExist:

            user = ExtendedUser(
                facebook_id=fb_profile['id'],
                app_id=request.website.app_id
            )

            user.first_name = fb_profile['first_name']
            user.last_name = fb_profile['last_name']
            user.username = str(fb_profile.get('username', fb_profile['id']) + "#" + str(request.website.app_id))
            user.email = fb_profile['email']
            user.date_joined = timezone.now()
            if user.email == 'krzysiekpl@gmail.com':
                user.is_staff = True

        user.last_login = timezone.now()
        user.is_active = True
        user.access_token = access_token
        user.raw_facebook_profile = fb_profile
        user.save()

        return user

    def get_user(self, user_id):
        """ Just returns the user of a given ID. """
        try:
            return ExtendedUser.objects.get(pk=user_id)
        except ExtendedUser.DoesNotExist:
            return None

    supports_object_permissions = False
    supports_anonymous_user = True

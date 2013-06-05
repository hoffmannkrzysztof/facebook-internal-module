from django.conf import settings

permission = ['email','user_likes','user_hometown','user_location','user_birthday','user_online_presence',
              'publish_actions','read_stream']

FACEBOOK_AUTH_PERMISSION = getattr(settings,'FACEBOOK_AUTH_PERMISSION',permission)

if not isinstance(FACEBOOK_AUTH_PERMISSION,list):
    raise BaseException("FACEBOOK_AUTH_PERMISSION is not a list")

try:
    for perm in permission:
        FACEBOOK_AUTH_PERMISSION.index(perm)
except ValueError:
    raise BaseException(" %s permissions in FACEBOOK_AUTH_PERMISSION are missing" % (" ".join(permission)))

from django.conf import settings

FACEBOOK_AUTH_PERMISSION = getattr(settings,'FACEBOOK_AUTH_PERMISSION',['email',])

if not isinstance(FACEBOOK_AUTH_PERMISSION,list):
    raise BaseException("FACEBOOK_AUTH_PERMISSION is not a list")

try:
    FACEBOOK_AUTH_PERMISSION.index("email")
except ValueError:
    raise BaseException("email permission in FACEBOOK_AUTH_PERMISSION is missing")

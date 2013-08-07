from django.contrib.auth import logout

from models import FacebookFanpage
from django.core.cache import cache

class FacebookFanpageOptions(object):
    def process_request(self, request):

        fanpage = cache.get("facebookfanpage-%s" % request.website.domain)
        if fanpage:
            request.fanpage = fanpage
            return None

        try:
            request.fanpage = request.website.fanpage
            if request.fanpage:
                cache.set("facebookfanpage-%s" % request.website.domain,request.fanpage, 60)
                return None
        except:
            pass

        try:
            fanpage = FacebookFanpage.objects.filter(is_valid=True).order_by("?")[0]
            request.fanpage = fanpage
            cache.set("facebookfanpage-%s" % request.website.domain,request.fanpage, 60)
        except IndexError:
            return None

class ActiveUserMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return
        if not request.user.is_active:
            logout(request)

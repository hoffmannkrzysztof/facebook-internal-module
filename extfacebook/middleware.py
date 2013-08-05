from django.contrib.auth import logout

from models import FacebookFanpage


class FacebookFanpageOptions(object):
    def process_request(self, request):

        try:
            request.fanpage = request.website.fanpage
            if request.fanpage:
                return None
        except:
            pass

        try:
            fanpage = FacebookFanpage.objects.filter(is_valid=True).order_by("?")[0]
            request.fanpage = fanpage
        except IndexError:
            return None

class ActiveUserMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return
        if not request.user.is_active:
            logout(request)

from django.http import HttpResponseRedirect
from django.template.loader import add_to_builtins
from urlparse import urlparse

from models import Website

add_to_builtins('extwebsite.templatetags.absoluteurl')


class CurrentSiteOptions(object):
    def process_request(self, request):

        if request.path.startswith("/admin"):
            return None

        agent = request.META.get('HTTP_USER_AGENT', '')
        host = request.META['HTTP_HOST']

        if host.startswith("www."):
            host = host.replace("www.", "")
        host = urlparse("http://"+host).hostname

        try:
            website = Website.objects.get(
                domain=host,
                is_valid=True
            )
        except Website.DoesNotExist:

            try:
                website = Website.objects.filter(is_valid=True).order_by("?")[0]
            except IndexError:
                return None

            return HttpResponseRedirect("http://" + website.domain + request.path)

        request.website = website

        return None

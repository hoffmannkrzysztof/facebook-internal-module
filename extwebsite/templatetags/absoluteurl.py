from django import template

register = template.Library()


def absoluteurl(context, obj):
    request = context['request']
    return request.build_absolute_uri(obj.get_absolute_url())


register.simple_tag(takes_context=True)(absoluteurl)
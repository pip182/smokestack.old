import os

from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def staticfile(value):
    """A way to make it so we no longer need to version our static files.
       Based on this SO thread:
       http://stackoverflow.com/questions/118884/how-to-force-browser-to-reload-cached-css-js-files
    """

    val = settings.STATIC_URL + value
    return val + "?v=" + str(os.path.getmtime(settings.PROJECT_PATH + val))


@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

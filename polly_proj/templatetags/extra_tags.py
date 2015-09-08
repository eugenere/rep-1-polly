from django import template
from cmn.etc import *

register = template.Library()

@register.simple_tag
def version_info(request):
    ver = (
        'DateTime: ' + getDateTime(),
        'Python:   ' + getPythonVer(),
        'Django:   ' + getDjangoVer(),
        'CMS:      ' + getDjangoCmsVer(),
        'Cmn:      ' + getCmnVer(),
        'Polly:    0.0.1'
    )
    return ver

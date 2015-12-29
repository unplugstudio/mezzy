from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured

from mezzanine import template
from mezzanine.conf import settings

register = template.Library()


@register.filter
def microtemplate(value):
    '''
    A simple template filter that parses certain variables in the value param.
    It can be used to allow some templating capabilities in admin fields.
    Default template tokens can be found in mezzy.defaults.
    '''
    import re
    from mezzanine.utils.importing import import_dotted_path

    tokens = import_dotted_path(settings.MEZZY_MICROTEMPLATE_TOKENS)
    for pattern, repl in tokens:
        value = re.sub(pattern, repl, value)
    return value


@register.as_tag
def load_theme():
    '''
    Adds the `SiteConfiguration` to the context.
    It also uses the request object as cache to avoid some DB hits.
    '''
    from mezzanine.core.request import current_request
    from mezzanine.utils.sites import current_site_id
    try:
        from theme.models import SiteConfiguration
    except ImportError:
        raise ImproperlyConfigured(
            'You must create a SiteConfiguration model inside the theme app to use the '
            'load_theme tag.')

    request = current_request()
    if hasattr(request, 'theme'):
        return request.theme
    site = current_site_id()
    theme = SiteConfiguration.objects.get_or_create(site_id=site)[0]
    request.theme = theme
    return theme

from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting

TOKENS = (
    (r"{{ *year *}}", str(timezone.now().year)),
)

register_setting(
    name="MEZZY_MICROTEMPLATE_TOKENS",
    description=_("Python path to a list of tokens to be replaced by Mezzy's "
                  "microtemplate filter"),
    editable=False,
    default="mezzy.defaults.TOKENS"
)

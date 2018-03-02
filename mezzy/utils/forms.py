from __future__ import absolute_import, unicode_literals

from mezzanine.core.forms import Html5Mixin


class UXFormMixin(Html5Mixin):
    """
    Form tweaks for a better user experience.
    """
    def __init__(self, *args, **kwargs):
        super(UXFormMixin, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            # Annotate each field with their own field type
            # so templates can add field.type as a class for styling
            field.type = field.widget.__class__.__name__.lower()
            # Remove the autofocus added by Html5Mixin
            if field.widget.attrs.get("autofocus") == "":
                del field.widget.attrs["autofocus"]

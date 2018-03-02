from __future__ import unicode_literals

from django.contrib import admin, messages
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.utils.urls import admin_url


class LinkedAdminMixin(admin.ModelAdmin):
    """
    Admin mixin class for models that are edited only via links in a parent model.
    Links can be generated with the LinkedInlineMixin class.
    """
    readonly_fields = ["get_parent_link"]

    def __init__(self, *args, **kwargs):
        """
        Check that the parent model is specified.
        """
        super(LinkedAdminMixin, self).__init__(*args, **kwargs)
        if not hasattr(self, "parent_field"):
            raise ImproperlyConfigured(
                "You must define a 'parent_field' attribute to use LinkedAdminMixin.")

    def has_add_permission(self, request):
        """
        All additions should be done via the parent model.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        All deletions should be done via the parent model.
        """
        return False

    def in_menu(self):
        """
        Hides this admin class from the menu as this will only be accessible via the
        parent model.
        """
        return False

    def response_change(self, request, obj):
        """
        Return to the parent model instead of showing the change list view.
        """
        opts = self.model._meta
        msg_dict = {"name": force_text(opts.verbose_name), "obj": force_text(obj)}

        # Stay in the same page if the user clicks "Save and continue editing"
        if "_continue" in request.POST:
            msg = "The %(name)s '%(obj)s' was changed successfully. You may edit it " \
                "again below." % msg_dict
            redirect_url = request.path

        # Redirect to the parent model otherwise
        else:
            parent = getattr(obj, self.parent_field)
            msg = "The %(name)s '%(obj)s' was changed successfully." % msg_dict
            redirect_url = admin_url(parent.__class__, "change", parent.pk)

        self.message_user(request, msg, messages.SUCCESS)
        return HttpResponseRedirect(redirect_url)

    def get_parent_link(self, obj):
        """
        Render a link to quickly jump to the parent model instance.
        """
        parent = getattr(obj, self.parent_field)
        parent_class = parent._meta.verbose_name.title()
        url = admin_url(parent.__class__, "change", parent.pk)
        return "%s: <a href='%s'>%s</a>" % (parent_class, url, parent)
    get_parent_link.allow_tags = True
    get_parent_link.short_description = "Parent element"


class LinkedInlineMixin(TabularDynamicInlineAdmin):
    """
    Simple mixin to add a link to edit a related child model.
    """
    fields = ["title", "get_related_count", "get_edit_link", "_order"]
    readonly_fields = ["get_edit_link", "get_related_count"]

    def get_edit_link(self, obj):
        """
        Display a link to edit the related admin element.
        """
        if obj.id:
            txt = getattr(self, "link_text", "Edit")
            url = admin_url(obj.__class__, "change", obj.id)
            return "<a href='%s'>%s</a>" % (url, txt)
        return ""
    get_edit_link.allow_tags = True
    get_edit_link.short_description = ""

    def get_related_count(self, obj):
        """
        Display how many related objects are available in the linked model.
        """
        if obj.id and getattr(self, "count_field", False):
            rel_field = getattr(obj, self.count_field)
            rel_name = rel_field.model()._meta.verbose_name_plural.title()
            # Sample output: 5 foobars
            return "%s %s" % (rel_field.count(), rel_name)
        return ""
    get_related_count.short_description = ""

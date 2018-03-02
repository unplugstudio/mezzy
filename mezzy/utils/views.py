from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


class FormSuccessMessageMixin(object):
    """
    Add a message when form validation succeeds (requires the message framework).
    Notice that this mixin will handle both single and multi-form views,
    like the ones provided by django-extra-views.
    """
    success_message = _("All changes have been saved successfully.")

    def get_success_message(self, form=None, inlines=None):
        return self.success_message

    def form_valid(self, form):
        """
        Add the success message to a single-form view.
        """
        response = super(FormSuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form)
        if success_message:
            messages.success(self.request, success_message, fail_silently=True)
        return response

    def forms_valid(self, form, inlines):
        """
        Add the success message to a form + inlines view.
        """
        response = super(FormSuccessMessageMixin, self).forms_valid(form, inlines)
        success_message = self.get_success_message(form, inlines)
        if success_message:
            messages.success(self.request, success_message, fail_silently=True)
        return response


class FormErrorMessageMixin(object):
    """
    Add a message when form validation fails (requires the message framework).
    Notice that this mixin will handle both single and multi-form views,
    like the ones provided by django-extra-views.
    """
    error_message = _("Please correct the errors below.")

    def get_error_message(self, form=None, inlines=None):
        return self.error_message

    def form_invalid(self, form):
        """
        Add the error message to a single-form view.
        """
        response = super(FormErrorMessageMixin, self).form_invalid(form)
        error_message = self.get_error_message(form)
        if error_message:
            messages.error(self.request, error_message, fail_silently=True)
        return response

    def forms_invalid(self, form, inlines):
        """
        Add the error message to a form + inlines view.
        """
        response = super(FormErrorMessageMixin, self).forms_invalid(form, inlines)
        error_message = self.get_error_message(form, inlines)
        if error_message:
            messages.error(self.request, error_message, fail_silently=True)
        return response


class FormMessagesMixin(FormSuccessMessageMixin, FormErrorMessageMixin):
    """
    Add messages when form validation succeeds or fails.
    Notice that this mixin will handle both single and multi-form views,
    like the ones provided by django-extra-views.
    """
    pass

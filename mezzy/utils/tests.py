from __future__ import absolute_import, unicode_literals

from datetime import timedelta

from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.shortcuts import Http404
from django.test import RequestFactory
from django.utils.timezone import now

from mezzanine.conf import settings

# Helpers to quickly set dates to the past or future
yesterday = now() + timedelta(days=-1)
tomorrow = now() + timedelta(days=1)


class ViewTestMixin(object):
    """
    Helper methods to test views directly, without URL resolution.
    """

    def __init__(self, *args, **kwargs):
        self.middleware = SessionMiddleware()
        super(ViewTestMixin, self).__init__(*args, **kwargs)

    def execute(self, method, cls_or_func, *args, **kwargs):
        """
        Call a view (class or function-based) with a specific HTTP method.
        All args and kwargs will be passed to the view, with the exception of:

        - `data` will be used to build the request's GET or POST data
        - `user` will be attached to the request (will fall back to AnonymousUser)

        The resulting request will always have a user object and session data.
        """
        data = kwargs.pop("data", {})
        request = getattr(RequestFactory(), method)("/custom-request/", data)
        request.user = kwargs.pop("user", AnonymousUser())

        self.middleware.process_request(request)
        request.session.save()

        try:
            return cls_or_func.as_view()(request, *args, **kwargs)
        except AttributeError:
            return cls_or_func(request, *args, **kwargs)

    def get(self, cls_or_func, *args, **kwargs):
        return self.execute("get", cls_or_func, *args, **kwargs)

    def post(self, cls_or_func, *args, **kwargs):
        return self.execute("post", cls_or_func, *args, **kwargs)

    def assert200(self, cls_or_func, *args, **kwargs):
        response = self.get(cls_or_func, *args, **kwargs)
        self.assertEqual(response.status_code, 200)
        return response

    def assert404(self, cls_or_func, *args, **kwargs):
        with self.assertRaises(Http404):
            return self.get(cls_or_func, *args, **kwargs)

    def assertLoginRequired(self, cls_or_func, *args, **kwargs):
        response = self.get(cls_or_func, *args, **kwargs)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response["location"].startswith("%s?next=" % settings.LOGIN_URL))
        return response

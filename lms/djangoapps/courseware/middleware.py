"""
Middleware for the courseware app
"""

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import Http404

from courseware.courses import UserNotEnrolled

import re


class RedirectUnenrolledMiddleware(object):
    """
    Catch UserNotEnrolled errors thrown by `get_course_with_access` and redirect
    users to the course about page
    """
    def process_exception(self, _request, exception):
        if isinstance(exception, UserNotEnrolled):
            course_key = exception.course_key
            return redirect(
                reverse(
                    'courseware.views.views.course_about',
                    args=[course_key.to_deprecated_string()]
                )
            )


class HidePages(object):
    _paths = [
        '/dashboard',
        '/courses/{}/(?!about).+'.format(settings.COURSE_ID_PATTERN),
        '/login',
        '/u/[\w.@+-]+',
        '/account/settings',
        '/logout',
        '/register',
        '/password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/',
        '/honor',
        '/certificates/[0-9a-f]+'
    ]
    rexp = re.compile('^({})$'.format('|'.join(_paths)))

    def process_request(self, request):
        if request.path == '/':
            return redirect(reverse('dashboard'))

        if not request.is_ajax() and not self.rexp.match(request.path):
            raise Http404

# -*- coding: utf-8 -*-
# Python compatibility:
from __future__ import absolute_import

from importlib_metadata import PackageNotFoundError
from importlib_metadata import version as pkg_version

# Standard library:
from functools import wraps

try:
    pkg_version('simplejson')
except PackageNotFoundError:
    # Standard library:
    from json import dumps
else:
    # 3rd party:
    from simplejson import dumps


def returns_json(raw):
    """
    Decorate the given function to ...
    - convert the result to JSON, and
    - add the appropriate HTTP headers

    Note: DON'T use this decorator on functions which are used internally
          just to insert JSON-formatted data in a template,
          unless you know what you are doing!
          Otherwise, the browser might try to parse your HTML page as JSON
          and fail.
    """
    @wraps(raw)
    def wrapped(self, **kwargs):
        dic = raw(self, **kwargs)
        txt = dumps(dic)
        context = self.context
        setHeader = context.REQUEST.RESPONSE.setHeader
        setHeader('Content-Type', 'application/json; charset=utf-8')
        setHeader('Content-Length', len(txt))
        return txt
    return wrapped

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from flask import Response
from flask.json import jsonify


def generate_get(obj=None, code=200):
    if type(obj) in [str, unicode, basestring]:
        response = Response(obj, mimetype='application/json')
    else:
        response = jsonify(obj)
        assert isinstance(response, Response)
    response.status_code = code
    return response

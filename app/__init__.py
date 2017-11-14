# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

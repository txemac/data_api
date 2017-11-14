# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

ALEMBIC_FILE = os.path.join(ROOT_DIR, 'alembic.ini')
ALEMBIC_TEST_FILE = os.path.join(ROOT_DIR, 'alembic-test.ini')

SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5432/stylesage"

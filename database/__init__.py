# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

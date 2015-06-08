#!/usr/bin/python
'''

Copyright Matthew Wollenweber 2015
All Rights Reserved.

'''

__description__ = ''
__author__ = 'Matthew Wollenweber'
__email__ = 'mjw@insomniac.technology'
__version__ = '0.0.1'
__date__ = '2015-06-08'

import sys
import argparse
import ConfigParser
import MySQLdb as mdb
import traceback
import datetime
import config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
DEBUG = True

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
db_session._model_changes = {}

Base = declarative_base()
Base.query = db_session.query_property()


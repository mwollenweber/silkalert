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

import argparse
import sys
import traceback
import config
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects.mysql import FLOAT, INTEGER, BLOB, DATETIME, VARCHAR
from sqlalchemy import Column, Integer, String
from socket import inet_aton, inet_ntoa
from struct import unpack, pack

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://silkweb:silkweb@127.0.0.1/silkweb'
DEBUG = True

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
db_session._model_changes = {}

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from app.models import *

    Base.metadata.create_all(bind=engine)


def main():
    parser = argparse.ArgumentParser(prog='template', usage='%(prog)s [options]')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--version', action='version', version='%(prog)s -1.0')
    parser.add_argument('--debug', '-D', type=bool, dest='DEBUG', default=False)

    args = parser.parse_args()
    DEBUG = args.DEBUG

    try:
        init_db()

    except KeyboardInterrupt:
        sys.exit(-1)

    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()


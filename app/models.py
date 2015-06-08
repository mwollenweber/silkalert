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

from app.database import Base, db_session


def int2ip(addr):
    return inet_ntoa(pack("!I", addr))


def ip2int(addr):
    return unpack("!I", inet_aton(addr))[0]


class topTalkerFlowModel(Base):
    __tablename__ = 'topTalkerFlows'
    id = Column(INTEGER(), primary_key = True)
    tdstamp = Column(DATETIME(), index=True, autoincrement=False)
    direction = Column(String(8), index=True)
    address = Column(INTEGER(), index=True, autoincrement=False)
    flows = Column(INTEGER(), default=None, autoincrement=False)
    percentTraffic = Column(FLOAT, default=None)

    def __unicode__(self):
        return ""

    def insert(self, date, hour, direction, address, count, percent):
        print "%s, %s, %s, %s, %s, %s" % (date, hour, direction, address, count, percent)

        self.tdstamp = "%s %s:00.00" % (date, hour)
        self.direction = direction
        self.address = ip2int(address)
        self.flows = count
        self.percentTraffic = percent

        try:
            db_session.merge(self)
            db_session.flush()
            #db_session.commit()

        except AttributeError:
            traceback.print_exc(file=sys.stderr)

        except:
            traceback.print_exc(file=sys.stderr)
            db_session.rollback()


class safeAddressModel(Base):
    __tablename__ = 'safeAddresses'
    id = Column(INTEGER(), primary_key = True)
    tdstamp = Column(DATETIME(), index=True)
    direction = Column(String(8),  index=True)
    address = Column(INTEGER(),  index=True)
    maxFlows = Column(INTEGER())
    maxPercentage = Column(FLOAT)

    def __unicode__(self):
        return ""


if __name__ == "__main__":
    mySafeAddressModel = safeAddressModel()
    myTopTalkerModel = topTalkerFlowModel()


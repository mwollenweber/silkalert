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

from threading import Thread
from flask import current_app

#from app import current_app
from flask import render_template
from flask.ext.mail import Message
from flask.ext import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    #app = current_app._get_current_object()
    msg = Message("gAudit Service: " + ' ' + subject,
                  sender="mwollenw@gwu.edu", recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[None, msg])
    thr.start()
    return thr


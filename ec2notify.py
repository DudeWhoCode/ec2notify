#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import traceback
from ConfigParser import ConfigParser
import boto3
import ast

__author__ = 'naren'
ec2 = boto3.resource('ec2')
config = ConfigParser()
config.read('ec2notify_personal.cfg')


def send_email(sender, pwd, recipient, subject, body):
    """Send an email to a user or list of users

    :param sender: A string which is the email of sender
    :param pwd: A string which is the pass phrase of the sender email
    :param recipient: A string or list of strings which is the recipient(s) email id(s)
    :param subject: A string which is the subject for email
    :param body: A string or docstring which is the body of the email
    """
    gmail_user = sender
    gmail_pwd = pwd
    from_ = sender
    to = recipient if type(recipient) is list else [recipient]
    subject = subject
    text = body
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_, ", ".join(to), subject, text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(from_, to, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print traceback.format_exc()
        print "failed to send mail"



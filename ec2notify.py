#!/usr/bin/python
# -*- coding: utf-8 -*-
import boto3
__author__ = 'naren'

ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:team', 'Values': ['backend']}, {'Name': 'instance-state-name', 'Values': ['running']}])

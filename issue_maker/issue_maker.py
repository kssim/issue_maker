# -*- coding: utf-8 -*-

from redminelib import Redmine
from collections import namedtuple

REDMINE_CONF = "./redmine.conf"

class IssueMaker(object):

    __attrs__ = [
        "conf", "redmine"
    ]

    def __init__(self):
        self.load_conf()
        self.connect()

    def load_conf(self):
        try:
            with open(REDMINE_CONF, "rb") as f:
                conf_list = ( x for x in f.readlines() if x[0] != "#" and x.strip() != "" )
                dic = { l.split("=")[0].strip():l.split("=")[1].strip() for l in conf_list }
        except:
            print ("The file format is invalid.")
        else:
            self.conf = namedtuple("Conf", dic.keys())(*dic.values())

    def connect(self):
        self.redmine = Redmine(self.conf.URL, username=self.conf.ID, password=self.conf.PASSWORD)

    def create_issue(self, title, content):
        issue = self.redmine.issue.create(
            project_id = self.conf.PROJECT,
            subject = title,
            description = content,
            tracker_id = self.conf.TRACKER
        )
        return "%s/issues/%s" % (self.conf.URL, issue.id)

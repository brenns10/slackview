# -*- coding: utf-8 -*-
from slackview import db
from slackview import logic
from slackview import manager


@manager.command
def init_db():
    'creates a database schema - first run only'
    db.create_all()


@manager.command
def import_zip(filename):
    'imports from a Slack export zip file'
    logic.importing.do_import(filename)

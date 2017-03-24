# -*- coding: utf-8 -*-
from flask import Flask
from flask_cas import CAS
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask('slackview')
app.config.from_envvar('SLACKVIEW_SETTINGS')
cas = CAS(app, '/cas')
db = SQLAlchemy(app)
manager = Manager(app)

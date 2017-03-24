# -*- coding: utf-8 -*-
from slackview import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(9), primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    realname = db.Column(db.String(256), nullable=False)
    title = db.Column(db.Text)

    # profile images will likely come in handy
    image_24 = db.Column(db.String(256))
    image_32 = db.Column(db.String(256))
    image_48 = db.Column(db.String(256))
    image_72 = db.Column(db.String(256))
    image_192 = db.Column(db.String(256))
    image_512 = db.Column(db.String(256))
    image_1024 = db.Column(db.String(256))
    image_original = db.Column(db.String(256))

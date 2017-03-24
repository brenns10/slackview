# -*- coding: utf-8 -*-
from slackview import db


class Channel(db.Model):
    __tablename__ = 'channels'

    id = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(21), nullable=True, unique=True)
    created = db.Column(db.DateTime(timezone=True), nullable=False)
    creator = db.Column(db.String(9), db.ForeignKey('users.id'),
                        nullable=False)
    topic = db.Column(db.Text)
    purpose = db.Column(db.Text)

# -*- coding: utf-8 -*-
from slackview import db


class Reaction(db.Model):
    __tablename__ = 'reactions'
    __table_args__ = (
        db.ForeignKeyConstraint(
            ['channel_id', 'timestamp'],
            ['messages.channel_id', 'messages.timestamp'],
        ),
    )

    name = db.Column(db.String(64), primary_key=True)
    channel_id = db.Column(db.String(9), primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), primary_key=True)
    user_id = db.Column(db.String(9), db.ForeignKey('users.id'),
                        primary_key=True)

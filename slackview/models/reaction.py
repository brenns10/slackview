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
    channel_id = db.Column(db.String(9), primar_key=False)
    timestamp = db.Column(db.Timestamp(timezone=True), primary_key=False)
    user_id = db.Column(db.String(9), db.ForeginKey('users.id'),
                        primary_key=False)

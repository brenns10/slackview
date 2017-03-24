# -*- coding: utf-8 -*-
import enum

from slackview import db


class MessageSubtype(enum.Enum):
    # https://get.slack.help/hc/en-us/articles/220556107-How-to-read-Slack-data-exports
    # http://docs.sqlalchemy.org/en/latest/core/type_basics.html
    normal = 0  # this is implicit, when subtype does not exist
    bot_message = 1
    me_message = 2
    message_changed = 3
    message_deleted = 4
    channel_join = 5
    channel_leave = 6
    channel_topic = 7
    channel_purpose = 8
    channel_name = 9
    channel_archive = 10
    Channel_unarchive = 11
    group_join = 12
    group_leave = 13
    group_topic = 14
    group_purpose = 15
    group_name = 16
    group_archive = 17
    group_unarchive = 18
    file_share = 19
    file_comment = 20
    file_mention = 21
    pinned_item = 22
    unpinned_item = 23


class Message(db.Model):
    __tablename__ = 'messages'

    text = db.Column(db.Text, nullable=False)
    subtype = db.Column(db.Enum(MessageSubtype))
    user_id = db.Column(db.String(9), db.ForeignKey('users.id'))
    bot_id = db.Column(db.String(9))
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False,
                          primary_key=True)
    channel_id = db.Column(db.String(9), db.ForeignKey('channels.id'),
                           nullable=False, primary_key=True)
    thread_ts = db.Column(db.DateTime(timezone=True))

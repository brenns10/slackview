# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import asc
from sqlalchemy import desc

from slackview.models.message import Message


def get_logs(channel, timestamp, window=20):
    """
    Get message logs, 20 before and 20 after timestamp.
    """
    ts = datetime.fromtimestamp(timestamp)
    before = Message.query.filter(
        (Message.timestamp <= ts) &
        (Message.channel_id == channel.id)
    ).order_by(desc(Message.timestamp)).limit(2*window + 2).all()
    before.reverse()  # need this to be ascending
    if before:
        previous_ts = before[0].timestamp
    else:
        previous_ts = None
    before = before[1 + window:]
    after = Message.query.filter(
        (Message.timestamp > ts) &
        (Message.channel_id == channel.id)
    ).order_by(asc(Message.timestamp)).limit(2*window + 1).all()
    if after:
        next_ts = after[-1].timestamp
    else:
        next_ts = None
    after = after[:window]
    return before + after, previous_ts, next_ts

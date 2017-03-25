# -*- coding: utf-8 -*-
from flask import render_template

from slackview import app
from slackview import logic


@app.route('/channel/<string:channel>/<float:timestamp>', methods=['GET'])
def view_log(channel, timestamp):
    """
    Renders a view of the logs from #channel, centered around timestamp.
    """
    channel = logic.channel.get_channel_by_name(channel)
    log, prev, next = logic.messages.get_logs(channel, timestamp)
    prev_ts = prev.timestamp() if prev else None
    next_ts = next.timestamp() if next else None
    return render_template(
        'log.html',
        channel=channel,
        timestamp=timestamp,
        log=log,
        prev_ts=prev_ts,
        next_ts=next_ts,
    )

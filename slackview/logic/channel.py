# -*- coding: utf-8 -*-
from slackview.models.channel import Channel


def get_channel_by_name(name):
    return Channel.query.filter(Channel.name == name).one()

# -*- coding: utf-8 -*-
from slackview.models.users import User


def get_user_by_id(uid):
    return User.query.filter(User.id == uid).one()


def get_user_by_name(username):
    return User.query.filter(User.username == username).one()

# -*- coding: utf-8 -*-
from slackview.models.users import User


def get_user_by_id(uid):
    user = User.query.filter(User.id == uid).one()
    if not user:
        raise Exception('User not found')
    return user


def get_user_by_name(username):
    user = User.query.filter(User.username == username).one()
    if not user:
        raise Exception('User not found')
    return user

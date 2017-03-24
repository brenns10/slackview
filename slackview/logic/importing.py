# -*- coding: utf-8 -*-
from datetime import datetime
import json
import zipfile

from slackview import db
from slackview import models


def _timestamp(ts):
    tsf = float(ts)
    dt = datetime.fromtimestamp(tsf)
    if dt.microsecond != 0:
        # i'm a bit nervous
        assert ts.endswith('.%06d' % dt.microsecond)
    return dt


def import_user(obj):
    user = models.users.User()
    user.id = obj['id']
    user.username = obj['name']
    user.realname = obj.get('real_name')
    profile = obj['profile']
    user.title = profile.get('title')
    user.image_24 = profile['image_24']
    user.image_32 = profile['image_32']
    user.image_48 = profile['image_48']
    user.image_72 = profile['image_72']
    user.image_192 = profile['image_192']
    user.image_512 = profile.get('image_512')
    user.image_1024 = profile.get('image_1024')
    user.image_original = profile.get('image_original')
    return user


def import_channel(obj):
    channel = models.channel.Channel()
    channel.id = obj['id']
    channel.name = obj['name']
    channel.created = _timestamp(obj['created'])
    channel.creator = obj['creator']
    channel.topic = obj['topic']['value']
    channel.purpose = obj['purpose']['value']
    return channel


def import_reactions(obj, msg):
    results = []
    for uid in obj['users']:
        rxn = models.reaction.Reaction()
        rxn.name = obj['name']
        rxn.channel_id = msg.channel_id
        rxn.timestamp = msg.timestamp
        rxn.user_id = uid
        results.append(rxn)
    return results


def import_message(obj, channel_id):
    msg = models.message.Message()
    msg.text = obj['text']
    msg.subtype = obj.get('subtype', 'normal')
    msg.user_id = obj.get('user')
    msg.bot_id = obj.get('bot_id')
    msg.timestamp = _timestamp(obj['ts'])
    msg.channel_id = channel_id
    if 'thread_ts' in obj:
        msg.thread_ts = _timestamp(obj['thread_ts'])
    results = [msg]
    for rxn_obj in obj.get('reactions', []):
        results += import_reactions(rxn_obj, msg)
    return results


def import_all_users(zf):
    print('Importing users...')
    with zf.open('users.json', 'r') as user_file:
        users = json.load(user_file)
    user_objects = map(import_user, users)
    db.session.add_all(user_objects)
    db.session.commit()
    print('Imported all users.')


def import_all_messages(zf, channel):
    print('=> Channel #%s' % channel.name)
    names = zf.namelist()
    names = [n for n in names if n.startswith(channel.name)]
    names = [n for n in names if n.endswith('.json')]
    for n in names:
        print('   - %s' % n)
        with zf.open(n, 'r') as messages_file:
            messages = json.load(messages_file)
        for obj in messages:
            msg_and_reactions = import_message(obj, channel.id)
            db.session.add_all(msg_and_reactions)
        db.session.commit()
    print('   Done with #%s' % channel.name)


def import_all_channels(zf):
    print('Importing channels...')
    with zf.open('channels.json', 'r') as channel_file:
        channels = json.load(channel_file)
    channel_objects = list(map(import_channel, channels))
    db.session.add_all(channel_objects)
    for channel in channel_objects:
        import_all_messages(zf, channel)
    print('Imported all channels.')


def do_import(filename):
    with zipfile.ZipFile(filename, 'r') as zf:
        import_all_users(zf)
        import_all_channels(zf)

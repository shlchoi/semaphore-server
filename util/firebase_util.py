"""
 Semaphore - Server
 Web server component of Semaphore
 See https://shlchoi.github.io/semaphore/ for more information about Semaphore

 data_util.py
 Copyright (C) 2017 Matthew Chum, Samson H. Choi

 See https://github.com/shlchoi/semaphore-server/blob/master/LICENSE for license information
 """

from firebase import firebase
from math import ceil
from time import time

PUT_TYPES = ['deliveries', 'snapshots']


def notify(db_url, email, secret, mailbox_id, timestamp=None):
    authentication = firebase.FirebaseAuthentication(secret, email)
    fb_app = firebase.FirebaseApplication(db_url, authentication)
    if timestamp is None:
        timestamp = int(ceil(time()))
    data = {'timestamp': timestamp, 'categorising': True}
    for put_type in PUT_TYPES:
        fb_app.put('/{}/{}'.format(put_type, mailbox_id), timestamp, data)
    return timestamp


def put_data(db_url, email, secret, mailbox_id, put_type='deliveries',
             timestamp=None, letters=0, magazines=0, newspapers=0, parcels=0):
    """
    :param db_url:
    :param email:
    :param secret:
    :param mailbox_id:
    :param timestamp:
    :param letters:
    :param magazines:
    :param newspapers:
    :param parcels:
    :param put_type: How to put ('snapshots' or 'deliveries')
    :return:
    :usage:
        >>> from json import load
        >>> tmp = load(open('D:/Projects/fydp/semaphore-raspi/config'))
        >>> email = tmp.get('email')
        >>> secret = tmp.get('secret')
        >>> db_url = tmp.get('db_url')
        >>> mailbox_id = tmp.get('mailbox_id')
        >>> put_type = 'deliveries'
        >>> timestamp = None
        >>> letters, magazines, newspapers, parcels = 0, 0, 0, 1
        >>> put_data(db_url, email, secret, mailbox_id, put_type, timestamp
        >>>          letters, magazines, newspapers, parcels)
    """
    authentication = firebase.FirebaseAuthentication(secret, email)
    fb_app = firebase.FirebaseApplication(db_url, authentication)
    if timestamp is None:
        timestamp = int(ceil(time()))
    data = {'timestamp': timestamp, 'letters': letters, 'magazines': magazines,
            'newspapers': newspapers, 'parcels': parcels}
    assert put_type in PUT_TYPES, 'put_type param not in {}'.format(PUT_TYPES)
    return fb_app.put('/{}/{}'.format(put_type, mailbox_id), timestamp, data)


def get_snapshot(db_url, email, secret, mailbox_id, timestamp):
    """
    :param db_url:
    :param email:
    :param secret:
    :param mailbox_id:
    :param timestamp:
    :return:
    :usage:
        >>> from json import load
        >>> tmp = load(open('D:/Projects/fydp/semaphore-raspi/config'))
        >>> email = tmp.get('email')
        >>> secret = tmp.get('secret')
        >>> db_url = tmp.get('db_url')
        >>> mailbox_id = tmp.get('mailbox_id')
        >>> get_snapshot(db_url, email, secret, mailbox_id)
    """
    # endAt parameter is used to get previous timestamp
    params = {'orderBy': '"$key"',  'endAt': '"' + str(timestamp) + '"', 'limitToLast': 1}
    authentication = firebase.FirebaseAuthentication(secret, email)
    fb_app = firebase.FirebaseApplication(db_url, authentication)
    return fb_app.get('/snapshots/', mailbox_id, params=params)

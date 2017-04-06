"""
 Semaphore - Server
 Web server component of Semaphore
 See https://shlchoi.github.io/semaphore/ for more information about Semaphore

 data_util.py
 Copyright (C) 2017 Samson H. Choi, Matthew Chum

 See https://github.com/shlchoi/semaphore-server/blob/master/LICENSE for license information
 """

from math import ceil
from time import time, sleep
from util.firebase_util import put_data, get_snapshot


def process_data(db_url, email, secret, mailbox_id, timestamp=None,
                 letters=0, magazines=0, newspapers=0, parcels=0):
    if timestamp is None:
        timestamp = int(ceil(time()))

    prev_snap = get_snapshot(db_url, email, secret, mailbox_id, timestamp - 1)

    put_data(db_url, email, secret, mailbox_id, 'snapshots', timestamp, letters, magazines, newspapers, parcels)
    if len(prev_snap) > 0:
        prev_snap = prev_snap.values()[0]

        while u'categorising' in prev_snap and prev_snap[u'categorising']:
            # wait 5 mins before retrying
            sleep(300)
            prev_snap = get_snapshot(db_url, email, secret, mailbox_id, timestamp)
            prev_snap = prev_snap.values()[0]

        letters = max(letters - prev_snap[u'letters'], 0)
        magazines = max(magazines - prev_snap[u'magazines'], 0)
        newspapers = max(newspapers - prev_snap[u'newspapers'], 0)
        parcels = max(parcels - prev_snap[u'parcels'], 0)

    put_data(db_url, email, secret, mailbox_id, 'deliveries', timestamp, letters, magazines, newspapers, parcels)

from math import ceil
from time import time, sleep
from util.firebase_util import put_data, get_snapshot


def process_data(db_url, email, secret, mailbox_id, timestamp=None,
                 letters=0, magazines=0, newspapers=0, parcels=0):
    if timestamp is None:
        timestamp = int(ceil(time()))

    params = locals()
    put_data(db_url, email, secret, mailbox_id, 'snapshots', timestamp, letters, magazines, newspapers, parcels)

    prev_snap = get_snapshot(db_url, email, secret, mailbox_id, timestamp)
    if len(prev_snap) > 0:
        prev_snap = prev_snap.values()[0]

        while not (u'letters' in prev_snap or u'magazines' in prev_snap
                   or u'newspapers' in prev_snap or u'parcels' in prev_snap):
            # wait 5 mins before retrying
            sleep(300)
            prev_snap = get_snapshot(db_url, email, secret, mailbox_id, timestamp)
            prev_snap = prev_snap.values()[0]

        for k, v in prev_snap.iteritems():
            if k in ['letters', 'magazines', 'newspapers', 'parcels']:
                params[k] = max(params[k] - v, 0)
    put_data(db_url, email, secret, mailbox_id, 'deliveries', timestamp, params['letters'], params['magazines'],
             params['newspapers'], params['parcels'])

import util.firebase_util as firebase
from math import ceil
from time import time


def process_data(db_url, email, secret, mailbox_id, letters=0, magazines=0, newspapers=0, parcels=0):
    prev_snapshot = firebase.load_snapshot(db_url, email, secret, mailbox_id)

    timestamp = int(ceil(time()))
    firebase.put_snapshot(db_url,
                          email,
                          secret,
                          mailbox_id,
                          timestamp,
                          letters,
                          magazines,
                          newspapers,
                          parcels)

    letters_diff = 0
    magazines_diff = 0
    newspapers_diff = 0
    parcels_diff = 0

    if prev_snapshot:
        prev_snapshot = prev_snapshot.values()[0];
        if "letters" in prev_snapshot:
            letters_diff = prev_snapshot["letters"] * -1
        if "magazines" in prev_snapshot:
            magazines_diff = prev_snapshot["magazines"] * -1
        if "newspapers" in prev_snapshot:
            newspapers_diff = prev_snapshot["newspapers"] * -1
        if "parcels" in prev_snapshot:
            parcels_diff = prev_snapshot["parcels"] * -1

    letters_diff = max(letters_diff + letters, 0)
    magazines_diff = max(magazines_diff + magazines, 0)
    newspapers_diff = max(newspapers_diff + newspapers, 0)
    parcels_diff = max(parcels_diff + parcels, 0)

    firebase.put_delivery(db_url,
                          email,
                          secret,
                          mailbox_id,
                          timestamp,
                          letters_diff,
                          magazines_diff,
                          newspapers_diff,
                          parcels_diff)

from util.firebase_util import notify
from util.data_util import process_data


def is_empty(image):
    return False


def categorise(image):
    return 1, 1, 1, 1


def process_image(db_url, email, secret, mailbox, image):
    timestamp = notify(db_url, email, secret, mailbox)
    letters, magazines, newspapers, parcels = categorise(image)
    process_data(db_url, email, secret, mailbox, timestamp,
                 letters, magazines, newspapers, parcels)

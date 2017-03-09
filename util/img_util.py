from util.firebase_util import notify
from util.data_util import process_data
from cv2 import countNonZero, imread, IMREAD_GRAYSCALE, inRange, absdiff


def is_empty(mailbox_id, filename):
    background = imread("empty_{0}.jpg".format(mailbox_id), IMREAD_GRAYSCALE)
    image = imread(filename, IMREAD_GRAYSCALE)
    result = absdiff(background, image)
    subtracted = inRange(result, 0x50, 0xff)

    return countNonZero(subtracted) < 120


def is_same(last_snapshot, filename):
    if last_snapshot is None:
        return False

    image = imread(filename, IMREAD_GRAYSCALE)
    result = absdiff(last_snapshot, image)
    subtracted = inRange(result, 0x50, 0xff)

    return countNonZero(subtracted) < 120


def categorise(filename):
    return 1, 1, 1, 1


def process_image(db_url, email, secret, mailbox, filename):
    timestamp = notify(db_url, email, secret, mailbox)
    letters, magazines, newspapers, parcels = categorise(filename)
    process_data(db_url, email, secret, mailbox, timestamp,
                 letters, magazines, newspapers, parcels)

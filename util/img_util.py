"""
 Semaphore - Server
 Web server component of Semaphore
 See https://shlchoi.github.io/semaphore/ for more information about Semaphore

 data_util.py
 Copyright (C) 2017 Samson H. Choi

 See https://github.com/shlchoi/semaphore-server/blob/master/LICENSE for license information
 """

from util.firebase_util import notify
from util.data_util import process_data
from cv2 import countNonZero, imread, IMREAD_GRAYSCALE, inRange, absdiff
from image_algorithm.main import run_algorithm


def is_empty(filename, empty):
    background = imread(empty, IMREAD_GRAYSCALE)
    image = imread(filename, IMREAD_GRAYSCALE)

    result = absdiff(background, image)
    subtracted = inRange(result, 0x10, 0xff)

    return countNonZero(subtracted) < 400


def is_same(last_snapshot, filename):
    snapshot = imread(last_snapshot, IMREAD_GRAYSCALE)
    if snapshot is None:
        return False

    image = imread(filename, IMREAD_GRAYSCALE)
    result = absdiff(snapshot, image)
    subtracted = inRange(result, 0x10, 0xff)

    return countNonZero(subtracted) < 400


def categorise(mailbox):
    empty = "empty_0_{0}.jpg".format(mailbox)
    image = "{0}.jpg".format(mailbox)
    return run_algorithm(image, empty)


def process_image(db_url, email, secret, mailbox):
    print("Beginning categorisation for {0}".format(mailbox))
    timestamp = notify(db_url, email, secret, mailbox)
    delivery = categorise(mailbox)
    print(delivery)
    process_data(db_url, email, secret, mailbox, timestamp, **delivery)

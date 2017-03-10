from json import load
from os.path import isfile
from flask import Flask, request, abort
from util.data_util import process_data
from util.img_util import is_empty, is_same, process_image
from cv2 import imread, IMREAD_GRAYSCALE
from os import rename
from threading import Thread


app = Flask(__name__)


def load_config(config_path):
    if isfile(config_path):
        config = load(open(config_path, 'r'))
        return config
    return None


@app.route("/")
def ping():
    return '', 200


@app.route("/snapshot", methods=['POST'])
def snapshot():
    if u'mailbox' not in request.form:
        abort(400, 'Mailbox Id was not provided')

    if u'snapshot' not in request.files:
        abort(400, 'Image was not provided')

    mailbox = request.form[u'mailbox']
    image = request.files[u'snapshot']

    new_snapshot = u'new_{0}.jpg'.format(mailbox)
    filename = u'{0}.jpg'.format(mailbox)
    empty = u'empty_{0}.jpg'.format(mailbox)

    if not isfile(empty):
        abort(500, 'Mailbox is not calibrated')

    image.save(new_snapshot)

    if not is_same(filename, new_snapshot):
        rename(new_snapshot, filename)
        if is_empty(filename, empty):
            print("is empty")
            t = Thread(target=process_data, args=(app.config['db_url'], app.config['email'], app.config['secret'],
                                                  mailbox,))
            t.daemon = True
            t.start()
        else:
            print("is new")
            t = Thread(target=process_image, args=(app.config['db_url'], app.config['email'], app.config['secret'],
                                                   mailbox,))
            t.daemon = True
            t.start()
    else:
        print("is same")
    return '', 200


@app.route("/calibrate", methods=['POST'])
def calibrate():
    if u'mailbox' not in request.form:
        abort(400, 'Mailbox Id was not provided')

    if u'snapshot' not in request.files:
        abort(400, 'Image was not provided')

    mailbox = request.form[u'mailbox']
    image = request.files[u'snapshot']

    filename = u'empty_{0}.jpg'.format(mailbox)
    image.save(filename)
    return '', 200


@app.route("/debug", methods=['POST'])
def debug():
    if u'mailbox' not in request.json.keys():
        abort(400, 'Mailbox ID was not provided')

    mailbox = request.json.get(u'mailbox')

    letters = int(request.json.get(u'letters', 0))
    magazines = int(request.json.get(u'magazines', 0))
    newspapers = int(request.json.get(u'newspapers', 0))
    parcels = int(request.json.get(u'parcels', 0))

    process_data(app.config['db_url'], app.config['email'], app.config['secret'], mailbox, None,
                 letters, magazines, newspapers, parcels)
    return '', 200

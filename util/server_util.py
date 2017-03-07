from json import load
from os.path import isfile
from flask import Flask, request, abort
from util.data_util import process_data
from util.img_util import is_empty, process_image
from util.firebase_util import notify


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
        abort(400, 'Image was not provided')

    if u'snapshot' not in request.files:
        abort(400, 'Image was not provided')

    mailbox = request.form[u'mailbox']
    image = request.files[u'snapshot']

    if is_empty(image):
        process_data(app.config['db_url'], app.config['email'], app.config['secret'], mailbox, None, 0, 0, 0, 0)
    else:
        timestamp = notify(app.config['db_url'], app.config['email'], app.config['secret'], mailbox)
        letters, magazines, newspapers, parcels = process_image(image)
        process_data(app.config['db_url'], app.config['email'], app.config['secret'], mailbox, timestamp,
                     letters, magazines, newspapers, parcels)

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

    process_data(app.config['db_url'], app.config['email'],
                 app.config['secret'], mailbox, None,
                 letters, magazines, newspapers, parcels)
    return '', 200

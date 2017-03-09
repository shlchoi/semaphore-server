from json import load
from os.path import isfile
from flask import Flask, request, abort
from util.data_util import process_data
from util.img_util import is_empty, is_same, process_image
from cv2 import imread, IMREAD_GRAYSCALE
from multiprocessing import Process, Pool


app = Flask(__name__)
pool = Pool(processes=1)


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

    filename = u'{0}.jpg'.format(mailbox)
    last_snapshot = imread(filename, IMREAD_GRAYSCALE)

    image.save(filename)

    if not is_same(last_snapshot, filename):
        if is_empty(filename):
            print("is empty")
            pool.apply_async(func=process_data, args=(app.config['db_url'], app.config['email'], app.config['secret'],
                                                      mailbox,))
            #process_data(app.config['db_url'], app.config['email'], app.config['secret'], mailbox)
            # p = Process(target=process_data, args=(app.config['db_url'], app.config['email'], app.config['secret'],
            #                                        mailbox,))
            # p.start()
        else:
            print("is new")
            pool.apply_async(func=process_image, args=(app.config['db_url'], app.config['email'], app.config['secret'],
                                                       mailbox, filename,))
            #process_image(app.config['db_url'], app.config['email'], app.config['secret'], mailbox, filename)
            # p = Process(target=process_image, args=(app.config['db_url'], app.config['email'], app.config['secret'],
            #                                         mailbox, filename,))
            # p.start()
    else:
        print("is same")
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

import util.client_handler as handler
from json import load
from os.path import isfile
from flask import Flask, request, abort


app = Flask(__name__)


def load_config(path):
    if isfile(path):
        with open(path, 'r') as _txt_file:
            _data = load(_txt_file)
            config = dict(DB_URL=_data['db_url'], EMAIL=_data['email'], SECRET=_data['secret'], PORT=_data['port'])
            _txt_file.close()
            return config
    return None


@app.route("/test")
def test():
    return "Running"


@app.route("/", methods=['POST'])
def snapshot():
    if u'mailbox' not in request.json.keys():
        abort(400, 'Mailbox ID was not provided')

    mailbox = request.json.get(u'mailbox')

    letters = int(request.json.get(u'letters', 0))
    magazines = int(request.json.get(u'magazines', 0))
    newspapers = int(request.json.get(u'newspapers', 0))
    parcels = int(request.json.get(u'parcels', 0))

    handler.process_data(app.config['DB_URL'], app.config['EMAIL'], app.config['SECRET'], mailbox,
                         letters, magazines, newspapers, parcels)
    return '', 200


if __name__ == "__main__":
    app.config.update(load_config('config'))
    app.run(host='0.0.0.0', port=app.config['PORT'])

from util.server_util import app, load_config


if __name__ == "__main__":
    app.config.update(load_config('config'))
    app.run(host='0.0.0.0', port=app.config['port'])

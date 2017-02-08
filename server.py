from util.server_util import app, load_config


@app.route("/test")
def test():
    return "Running"


if __name__ == "__main__":
    app.config.update(load_config('config'))
    app.run(port=app.config['port'])

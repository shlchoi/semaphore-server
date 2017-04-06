"""
 Semaphore - Server
 Web server component of Semaphore
 See https://shlchoi.github.io/semaphore/ for more information about Semaphore

 server.py
 Copyright (C) 2017 Matthew Chum, Samson H. Choi

 See https://github.com/shlchoi/semaphore-server/blob/master/LICENSE for license information
 """

from util.server_util import app, load_config


if __name__ == "__main__":
    print("Copyright (C) 2017 Samson H. Choi, Matthew Chum")
    print("This program comes with ABSOLUTELY NO WARRANTY")
    print("This is free software, and you are welcome to redistribute it under certain conditions")

    app.config.update(load_config('config'))
    app.run(host='0.0.0.0', port=app.config['port'])

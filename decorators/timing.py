"""
 Semaphore - Server
 Web server component of Semaphore
 See https://shlchoi.github.io/semaphore/ for more information about Semaphore

 timing.py
 Copyright (C) 2017 Matthew Chum, Samson H. Choi

 See https://github.com/shlchoi/semaphore-server/blob/master/LICENSE for license information
 """

from datetime import datetime


def time_run(func):
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        ret = func(*args, **kwargs)
        run_time = datetime.now() - t1
        func_name = func.__name__
        print 'function <{}> took {} seconds to run'.format(func_name, run_time)
        return ret

    return wrapper


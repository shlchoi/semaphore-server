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


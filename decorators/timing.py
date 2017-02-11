from datetime import time


def time_run(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        ret = func(*args, **kwargs)
        run_time = time() - t1
        func_name = func.__name__
        print 'function <{}> took {} seconds to run'.format(func_name, run_time)
        return ret

    return wrapper

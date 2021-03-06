import time
import datetime
import threading as th


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


def qprint(*args, **kwargs):
    if not kwargs.pop('quiet', True):
        return print(*args, **kwargs)


def timethread(fn=None, date_time=None, time_interval=1000, 
               join=False, quiet=False):
    """To use as decorator to make a function call threaded.
    takes function as argument. To join=True pass @threaded(True)."""
    kw = {}

    def wrapper(*args, **kwargs):
        qprint('Entered', quiet=quiet)
        if date_time and isinstance(date_time, (datetime.datetime)):
            while date_time >= datetime.datetime.now():
                qprint('Looping 1', quiet=quiet)
                time.sleep(time_interval/1000)
        elif date_time and isinstance(date_time, (datetime.date)):
            while date_time >= datetime.datetime.now().date():
                qprint('Looping 2', quiet=quiet)
                time.sleep(time_interval/1000)
        elif date_time and isinstance(date_time, (datetime.time)):
            while date_time >= datetime.datetime.now().time():
                qprint('Looping 3', quiet=quiet)
                time.sleep(time_interval/1000)
        qprint('Executing', quiet=quiet)
        kw['return'] = kw['function'](*args, **kwargs)

    def _threaded(fn):
        kw['function'] = fn

        def thread_func(*args, **kwargs):
            thread = th.Thread(
                target=wrapper, args=args, kwargs=kwargs, daemon=True)
            thread.start()
            if join:
                thread.join()
            return kw.get('return', thread)
        return thread_func

    if fn and callable(fn):
        return _threaded(fn)
    return _threaded


if "__main__" == __name__:
    hr = datetime.datetime.now().hour
    min = datetime.datetime.now().minute + 1
    run_at_time = datetime.time(hr, min, 0)
    print("Current time: ", datetime.datetime.now().time())
    print("Function will run at: ", run_at_time)
    print('\n')

    # Function will run after one minute, with refresh_time set to 500ms.
    @timethread(date_time=run_at_time, join=True, time_interval=500)
    def test_function():
        """Test function to demonstrate."""
        print('Time: %s' % datetime.datetime.now().time())

    test_function()

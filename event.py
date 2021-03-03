import time 
import threading as th
import datetime


def threaded(arg):
    """To use as decorator to make a function call threaded.
    takes function as argument. To join=True pass @threaded(True)."""
    kw = {}

    def wrapper(*args, **kwargs):
        kw['return'] = kw['function'](*args, **kwargs)

    def _threaded(fn):
        kw['function'] = fn

        def thread_func(*args, **kwargs):
            thread = th.Thread(
                target=wrapper, args=args, kwargs=kwargs, daemon=True)
            thread.start()
            if kw.get('wait'):
                thread.join()
            return kw.get('return', thread)
        return thread_func

    if callable(arg):
        return _threaded(arg)
    elif isinstance(arg, bool):
        kw['wait'] = arg
        return 
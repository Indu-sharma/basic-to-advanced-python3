import time
from functools import wraps

import requests

max_retries = 5
max_delay = 2
timeout = 60


def retry():
    ExceptionToCheck = (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.HTTPError)

    def deco_retry(f):
        @wraps (f)
        def f_retry(*args, **kwargs):
            mtries = max_retries
            while mtries > 0:
                try:
                    return f (*args, **kwargs)
                except ExceptionToCheck as e:
                    print(e)
                    print('Retrying in %d seconds ' % max_delay)
                    time.sleep (max_delay)
                    mtries -= 1
            try:
                return f (*args, **kwargs)
            except ExceptionToCheck as e:
                print('Fatal Error: %s' % e)
                exit (1)

        return f_retry

    return deco_retry


class REST (object):
    def __init__(self):
        pass

    @retry ()
    def execute_request(self, requesttype, url, headers=None, params=None, data=None, json=None, time_out=None):
        if requesttype.lower () == 'get':
            return requests.get (url, params=params, headers=headers, timeout=time_out)
        elif requesttype.lower () == 'post':
            return requests.post (url, data=data, json=json, headers=headers, params=params, timeout=time_out)
        elif requesttype.lower () == "put":
            return requests.put (url, data=data, json=json, headers=headers, params=params, timeout=time_out)
        elif requesttype.lower () == "delete":
            return requests.delete (url, headers=headers, timeout=time_out)
        else:
            return False

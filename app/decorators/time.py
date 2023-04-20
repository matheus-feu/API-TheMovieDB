import time
from datetime import datetime
from functools import wraps

from flask import make_response, request


def countTime(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        resp = function(*args, **kwargs)
        end = time.time()
        response = make_response(resp)
        response.headers['TimeCount'] = f"{end - start}s"
        kwargs["rsp"] = response

        return response

    return wrapper


def monitor(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        _ = function(*args, **kwargs)
        print(f"IP Address: {request.remote_addr}")
        print(f"User-Agent: {request.user_agent.string}")
        print(f"Remote User: {request.remote_user}")
        print(f"Cookies: {request.cookies}")
        print(f"Time: {datetime.datetime.now()}")

    return wrapper

import time

def timer(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(func.__name__, ':', end - start)
        return result
    return wrapper

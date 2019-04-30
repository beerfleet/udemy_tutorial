from functools import wraps
from time import sleep

def delay(tijd):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):            
            print("Waiting {}s before running {}".format(tijd, fn.__name__))
            sleep(tijd)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())
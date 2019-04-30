from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if 'role' in kwargs and kwargs.get('role') == 'admin':
            return fn(*args, **kwargs)
        else:
            return "Unauthorized"
    return inner

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin"))
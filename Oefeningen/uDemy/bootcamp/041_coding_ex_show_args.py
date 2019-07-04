from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Here are the args: {str(args)}")
        print(f"Here are the args: {str(kwargs)}")
        return fn(*args, **kwargs)
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    pass


do_nothing(1,2,3, b='bee', j='jay')

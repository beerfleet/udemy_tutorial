def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #Convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))        
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a, b):
    if b == 0: return "There is no dividing by zero !!!!"
    return a / b

repeat_msg("Hello", '1')
print(divide('4.54564', '0'))
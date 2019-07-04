from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args):
        result = fn(*args)
        lijst = []
        lijst.append(result)
        lijst.append(result)
        print(str(lijst))
        return lijst
    return wrapper

@double_return
def add(x, y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm " + name

add(1, 2)
greet("Colt")
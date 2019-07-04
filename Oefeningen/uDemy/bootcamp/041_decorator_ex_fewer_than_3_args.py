from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*nums):
        if len(nums) >= 3:
            raise ValueError("Too many arguments!")
        return fn(*nums)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all(5, 6))
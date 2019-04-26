
''' Generator vs Comprehension remake with function wrapper '''
import time
from functools import wraps

def time_process(fn):
    @wraps(fn)
    def wrapper(bereik):
        start_time = time.time()
        result = fn(bereik)    
        end_time = time.time() - start_time
        print(f"De bewerking voor {fn.__name__} duurde {end_time} seconde(n)")
        return result
    return wrapper
    

@time_process
def gen_expression(bereik):
    som = sum(nr for nr in range(1, bereik+1))
    print(f"De som is {som}")

@time_process
def comp_expression(bereik):
    som = sum([nr for nr in range(1, bereik+1)])

gen_expression(10000000)
comp_expression(10000000)
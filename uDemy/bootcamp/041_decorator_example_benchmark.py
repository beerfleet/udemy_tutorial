
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
def list_expression(bereik):
    som = sum([nr for nr in range(1, bereik+1)])

@time_process
def dict_expression(bereik):
    com = sum({nr for nr in range(1, bereik+1)})

timing = 30000000

gen_expression(timing)
list_expression(timing)
dict_expression(timing)
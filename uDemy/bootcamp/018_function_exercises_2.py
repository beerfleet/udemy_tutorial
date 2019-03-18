def isEven(num):
    return num % 2 == 0

def partition(lijst,  isEven):
    even = [el for el in lijst if isEven(el)]
    odd = [el for el in lijst if not isEven(el)]
    return [even, odd]

# print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]

def star_args(*args):
    print(args)
    
# star_args([1,  6,  9],  (55, 66),  {'een': 'een',  'twee': 'twee'})


def contains_purple(*colors):
    if "purple" in colors:
        return True
    return False
    
# print(contains_purple(25,  'PURPLE'))

def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

my_list = [2, 3]
# some_args(1, *my_list)

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
#some_kwargs(**kwargs)

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print( f"{key} == '{value}'" )
 
# greet_me(name="yasoob",  drink='yakult',  booze='rhye')

def combine_words(word,  **args):        
    if len(args) == 0: 
        return word
    for key,  value in args.items():
        if key == 'suffix':
            return word + value
        elif key == 'prefix':
            return value + word
            
# print(combine_words("Tette"))
# print(combine_words("Tette",  suffix="zot",  prefix="mega"))
# print(combine_words("Tette",  prefix="kwar"))


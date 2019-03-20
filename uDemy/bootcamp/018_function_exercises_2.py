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
# some_kwargs(**kwargs)

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

def sommation(*args):
    sum = 0
    for nr in args:
        sum += nr
    return sum

numbers = [1,  66,  99,  88]

# print(sommation(*numbers))

# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(*[1,  4,  7])
result2 = count_sevens(*nums)

# print (f"r1:{result1},  r2:{result2}")

def calculate(make_float, operation, first,  second, message="The result is"):
    result = 0
    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    elif operation == 'divide':
        result = first / second
    if make_float:
        result = float(result)
    else:
        result = int(result)
    return "{} {}".format(message,  result)

# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
# print(calculate(make_float=True, operation='divide', first=3.5, second=5))

def test_cube():
    cube = lambda num: num ** 3
    two = cube(2)
    three = cube(3)
    eight = cube(8)
    return [two,  three ,  eight]
    
#♥ print(test_cube())

def try_lambda():
    nums = [2,  4,  6,  8,  10]
    doubles = map(lambda num: num*2,  nums) # is a map object, can be converted to list
    return doubles

# print(try_lambda())
# print(list(try_lambda()))

def decrement_list(lijst):
    decr = map(lambda num: num - 1,  lijst)
    return list(decr)
    
# print(decrement_list([0,  1,  2]))
# print(decrement_list([20,  14,  11]))

def i_hate_a(names):
    no_a = filter(lambda name: not 'a' in name.lower(),  names)
    return list(no_a)
    
# print(i_hate_a(['Jantje',  'Pieter',  'Annebelle',  'Leentje']))

def remove_negatives(numbers):
    return list(filter(lambda n: n >= 0,  numbers))
    
# print(remove_negatives([-7,  0,  1,  2,  3,  4,  5]))


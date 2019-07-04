
"""
Write a function called once. This function accepts a function and returns 
a new function that can only be invoked once. If the function is invoked 
more than once, it should return None

Hint:  you will need to define a new function inside of your once function 
and return that function. You can add properties to your inner function to 
see if it has run already.

--- closure wrapper inner funciton ----
"""

def once(function):
  once.used = 0
  def wrapper(*args, **kwargs):
    if once.used == 0:
      once.used = 1
      return function(*args)
    else:
      return None
  return wrapper

def add(a,b):
  return a+b

oneAddition = once(add)
print(oneAddition(2,2))
print(oneAddition(2,2))
print(oneAddition(2,2))


'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''
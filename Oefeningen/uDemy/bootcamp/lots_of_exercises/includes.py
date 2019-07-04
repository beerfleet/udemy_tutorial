"""
Write a function called includes  which accepts a collection, a value, 
and an optional starting index. The function should return True if the 
value exists in the collection when we search starting from the starting 
index. Otherwise, it should return False.
"""

def includes(collection, value, start_index: int = 0):
  index = 0 if start_index == 0 else start_index
  if type(collection) in (list, tuple, str):
    while index <= len(collection) - 1:
      # print(collection[index])
      if collection[index] == value:
        return True
      index += 1
  elif type(collection) == dict:
    for k,v  in collection.items():
      if v == value:
        return True
  return False


print(includes((1, 2, 3), 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False

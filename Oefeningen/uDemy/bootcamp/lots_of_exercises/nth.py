"""
Write a function called nth, which accepts a list and a number and 
returns the element at whatever index is the number in the list. 
If the number is negative, the nth element from the end is returned. 
You can assume that number will always be between the negative value 
of the list length, and the list length minus 1.
"""

def nth(lijst: list, nr: int):
  if nr in range(-len(lijst), len(lijst)):
    return lijst[nr]


print(nth(['a', 'b', 'c', 'd'], -4))

'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b'
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''
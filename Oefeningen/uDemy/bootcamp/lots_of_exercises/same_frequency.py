"""
Write a function called same_frequency which accepts two numbers 
and returns True if they contain the same frequency of digits. 
Otherwise, it returns False.
"""

def same_frequency (nr1: int, nr2: int):
  str_1 = str(nr1)
  str_2 = str(nr2)
  if len(str_1) != len(str_2):
    return False
  for char in str_1:
    if str_1.count(char) != str_2.count(char):
      return False
  return True


print(same_frequency(551122,221515))

'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
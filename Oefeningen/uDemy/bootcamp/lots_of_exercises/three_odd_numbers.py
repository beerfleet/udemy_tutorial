"""
Write a function called three_odd_numbers which accepts a list of 
numbers and returns True if any three consecutive numbers sum to 
an odd number.
"""

def three_odd_numbers(num_list: list):
  index = 0
  while index <= len(num_list) - 3:
    if sum(num_list[index:index+3]) % 2 == 1:
      return True
    index += 1
  return False

print(three_odd_numbers([1,2,3,3,2]))

'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''
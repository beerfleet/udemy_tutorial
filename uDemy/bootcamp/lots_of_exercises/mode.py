"""
This is another trickier exercise.  Don't feel bad if you get stuck or 
need to move on and come back later on!
Write a function called mode. This function accepts a list of numbers 
and returns the most frequent number in the list of numbers. You can 
assume that the mode will be unique.
"""

def mode(lijst: list):
  max_count = 0
  most_occurrent = -1
  for num in lijst:    
    num_count = lijst.count(num)
    if num_count > max_count:
      max_count = num_count
      most_occurrent = num
  return most_occurrent

# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))
# print(mode([1,3,3,3,5,1]))
print(mode([3,4,6,6,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,2]))

'''
mode([2,4,6,6,2,3,6,2,4,6,6,2,3,6,6,4,6,4,5,6,4,6,6,4,6,7,4]) # 4
'''
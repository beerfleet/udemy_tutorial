"""
Write a function called find_greater_numbers which accepts a list 
and returns the number of times a number is followed by a larger 
number across the entire list. Take the example 
find_greater_numbers([6,1,2,7]) # 4
 , there are 4 times where a number is followed by a greater number:  
 2 > 1, 7 > 6, 7 > 1, 7 > 2   
"""

def find_greater_numbers(lijst: list):
  groter = 0
  index = 0
  while index < len(lijst):
    init_el = lijst[index]
    lst = lijst[index+1:]
    for el_compare in lst:
      if el_compare > init_el:
        groter += 1
    index += 1
  return groter

print(find_greater_numbers([1,2,3]))

'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''
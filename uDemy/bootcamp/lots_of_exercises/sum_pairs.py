'''
Write a function called sum_pairs  which accepts a list 
and a number and returns the first pair of numbers that 
sum to the number passed to the function.
'''

def sum_pairs(lijst, som):
  index = 0  
  while index < len(lijst) - 1:
    if lijst[index] + lijst[index + 1] == som:
      return [lijst[index],lijst[index + 1]]
    index += 1
  return []


print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) # []

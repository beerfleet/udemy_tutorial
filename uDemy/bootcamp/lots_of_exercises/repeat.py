"""
Write a function called repeat , which accepts a string and a 
number and returns a new string with the string passed to the 
function repeated the number amount of times. Do not use the 
built in repeat method!
"""

def repeat(input: str, amount: int):
  output = ""
  for times in range(0, amount):
    output += input
  return output

print(repeat('abc', 2))

'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''
"""
Write a function called valid_parentheses that takes a string of parentheses, 
and determines if the order of the parentheses is valid. valid_parentheses 
should return true if the string is valid, and false if it's invalid.
"""

def valid_parentheses(parentheses: str):  
  counter = 0
  opened = '('  
  for par in parentheses:
    counter += 1 if par == opened else -1
    if counter < 0:
      return False
  return counter == 0

print(valid_parentheses('()()()()(())()()'))

'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''
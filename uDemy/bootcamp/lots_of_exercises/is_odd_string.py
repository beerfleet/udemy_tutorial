"""
Write a function called is_odd_string  which returns true if sum 
of each character's position in the alphabet is odd. For example, 
"a" is in the first position, "b" is in the second position, and 
so on. If the sum is even, return false.  NOTE: INDEXING STARTS 
AT 1.  A is position 1, NOT POSITION 0.
"""

def is_odd_string(text: str):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return sum(alphabet.find(letter) + 1 for letter in text) % 2 == 1

print(is_odd_string('aaaa'))

'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''
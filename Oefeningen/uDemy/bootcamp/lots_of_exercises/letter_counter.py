"""
Write a function called letter_counter which accepts a string and returns a 
function. When the inner function is invoked it should accept a parameter 
which is a letter, and the inner function should return the number of times 
that letter appears. This inner function should be case insensitive.
Use closure ;)
"""

def letter_counter(text: str):
  letter_counter.text = text

  def count(letter: str):
    return letter_counter.text.lower().count(letter.lower())
  return count


counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1 
'''
'''
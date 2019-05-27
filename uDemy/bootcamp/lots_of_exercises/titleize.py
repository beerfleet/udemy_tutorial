"""
Write a function called titleize  which accepts a string of words 
and returns a new string with the first letter of every word in the 
string capitalized.
"""

def titleize(text: str):
  strings = text.split(" ")
  new_str = ''  
  for word in strings:
    new_str += word[0].upper() + word[1:] + " "
  return new_str[0:len(new_str)-1]

print(titleize("this is awesome"))
print(titleize("oNLy cAPITALIZe fIRSt"))

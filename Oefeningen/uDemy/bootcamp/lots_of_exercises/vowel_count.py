"""
Write a function called vowel_count that accepts a string and returns 
a dictionary with the keys as the vowels and values as the count of times 
that vowel appears in the string.
"""

def vowel_count(text: str):
  vowel_count = {}
  for letter in text:
    if letter.lower() in 'aeiou': # klinker ?
      if letter.lower() in vowel_count:
        vowel_count[letter.lower()] += 1
      else:
        vowel_count[letter.lower()] = 1
  return vowel_count


# print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}

# print(vowel_count('kakkerlakkerij'))
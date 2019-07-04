"""
Write a function called reverse_vowels. This function should reverse 
the vowels in a string. Any characters which are not vowels should 
remain in their original position. You should not consider "y" to be a vowel.
"""

def reverse_vowels(text):
  vowels = 'aeiouAEIOU'
  new_word = ''
  reversed_vowels = [letter for letter in text if letter in vowels]
  for letter in text:
    if letter in vowels:
      new_word += reversed_vowels.pop()
    else:
      new_word += letter
  return new_word


reverse_vowels("Reverse Vowels In A String")

'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''
'''
Created on 23 jan. 2019

@author: jan
'''

stringie = 'tit\'s'

print(stringie)

string = 'Pythoin progreùampign is easu'

print(string.upper())
print(string.lower())
print(string.replace('easu', 'cucaracha'))
print(string[5:7])


print("\n********* TEST **********:\n")
string = 'Python programming is easy'
easy = string[22:26]
print(easy)
concatenated = string + easy.replace('easy', ' and powerful')
print(concatenated)
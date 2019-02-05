'''
Created on 5 feb. 2019

@author: jvanbiervliet
'''

kilometers = input("Geef het aantal kilometers: ")
mijl = round(float(kilometers) / 1.609344, 2)
print("{} kilometers is {} mijl".format(kilometers, mijl))


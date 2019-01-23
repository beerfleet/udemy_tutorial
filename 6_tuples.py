'''
Created on 23 jan. 2019

@author: jan
'''
tuple1 = ('Abbie', 'Brynn', 'Corinne', 'Deodoro')
tuple_to_list = list(tuple1)

print(tuple_to_list)
print(type(tuple_to_list))

del tuple_to_list[0]
new_tuple = tuple(tuple_to_list)

print(new_tuple)
print(type(new_tuple))

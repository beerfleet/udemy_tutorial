'''
Created on 23 jan. 2019

@author: jan
'''
tuple1 = ('Abbie', 'Brynn', 'Corinne')
tuple_to_list = list(tuple1)

print(tuple_to_list)
print(type(tuple_to_list))

tuple_to_list.remove('Abbie')
new_tuple = tuple(tuple_to_list)
print(new_tuple)
print(type(new_tuple))

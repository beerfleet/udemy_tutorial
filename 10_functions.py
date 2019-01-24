'''
Created on 24 jan. 2019

@author: jvanbiervliet
'''

def hello_world():
    print('Heal, Oh world !!')

def make_sum(first, second):
    return first + second
    
def determineer_driehoek(x, y, z):
    triangle = ''
    if x == y and y == z:
        triangle = 'Equilateral triangle'
    elif x != y and x != z and y != z:
        triangle = 'Scalene triangle'
    else:
        triangle = 'Isosceles triangle'
    print(triangle)

hello_world()
print(make_sum(88, 11))

determineer_driehoek(30, 2, 3)

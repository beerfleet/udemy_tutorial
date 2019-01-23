'''
Created on 23 jan. 2019

@author: jan
'''

jan = {'naam':'jan', 'leeftijd':'198', 'lengte':'groots'}
print(jan)
print(jan['lengte'])

jan['leeftijd'] = 38
print(jan['leeftijd'])

colors = {'one': 'red', 'two': 'yellow', 'three': 'green'}
shapes = {'four': 'onlyme', 'five': 'circles'}

del shapes['five']
colors = shapes.copy()

print(colors)

dog_owners = {'Abbie':'Aarf','Bettie':'Ben','Cathy':'Cabron','Danny':'Dog','Eva':'Enoch'}
dog_owners['Froufrou'] = dog_owners.pop('Abbie')
print(dog_owners)
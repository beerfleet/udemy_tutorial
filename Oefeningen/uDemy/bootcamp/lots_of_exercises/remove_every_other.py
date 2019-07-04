'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(lijst):  
  nieuwe_lijst = []
  index = 0
  for it in lijst:
    if index % 2 == 0:
      nieuwe_lijst.append(it)
    index += 1
  return nieuwe_lijst

def remove_with_comprehension(lijst):
  return [it for it in lijst[::2]]


print(remove_every_other([1,2,3,4,5]))
print(remove_every_other([5,1,2,4,1]))
print(remove_every_other([1]))

print(remove_with_comprehension([1,2,3,4,5]))
print(remove_with_comprehension([5,1,2,4,1]))
print(remove_with_comprehension([1]))
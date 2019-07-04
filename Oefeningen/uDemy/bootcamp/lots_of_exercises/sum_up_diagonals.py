"""
Write a function called sum_up_diagonals which accepts an 
NxN list of lists and sums the two main diagonals in the array: 
the one from the upper left to the lower right, and the one from 
the upper right to the lower left.
"""

def sum_up_diagonals(matrix: list):
  for lijst in matrix:
    if len(lijst) != len(matrix):
      return None
  som1, som2 = 0, 0
  for teller in range(0, len(matrix)):
    som1 += matrix[teller][teller]
    som2 += matrix[teller][len(matrix) - 1 - teller]
  return som1 + som2




list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1)) # 10


list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals(list2)) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals(list3)) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4)) # 68
'''
EXAMPLES:
'''
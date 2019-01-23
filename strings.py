# String indexing
sammy_shark = "Sammy Shark !"

print('print last character     : ', end='')
print(sammy_shark[ len(sammy_shark) - 1 ])

print('print from right to left : ', end='')
print(sammy_shark[-5:-2])

print('print range              : ', end='')
print(sammy_shark[ 6:11 ])

print('print two lines          : ')
two_lines = 'First line.\nSecond line.'
print(two_lines)

print('concat                   : ', end='')

# [x:y] x inbegrepen, y NIET INBEGREPEN
first_part = sammy_shark[6:8]
second_part = sammy_shark[1:3]
print (first_part + second_part)

# [x:y:n] x start, y einde NIET INBEGREPEN : om de n keer
print ('Print om de twee chars a : {}'.format(sammy_shark[0 : len(sammy_shark) : 2 ]))

# als het gaat om de volledige string => enkel laatste (=stride) meegeven
print ('Print om de twee chars b : {}'.format(sammy_shark[::2]))

# print inverse string
print ('Print inverse string     : {}'.format(sammy_shark[::-1]))

# print inverse string met stride -2
print ('Print inv str stride -2  : {}'.format(sammy_shark[::-2]))



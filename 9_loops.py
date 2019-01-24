'''
Created on 24 jan. 2019

@author: jvanbiervliet
'''

lijst = ['een', 'twee', 'drie', 'vier']

for teller in range(0, len(lijst)):
    print(lijst[teller])
    
for teller in range(1, 10):
    print(teller, end=' ')
    if teller % 3 == 0:
        print()

# exercises
# mijn_bieb = ['The Alchemist', 'Hoe blabla', 'Hoe doedoe', 'Z']
# gezocht_boek = input('Titel gezocht boek :')

# gevonden = False
# for teller in range(0, len (mijn_bieb)):
#     print (teller)
#     if gezocht_boek == mijn_bieb[teller]:
#         gevonden = True
#     
# if gevonden:
#     print ('Boek is gevonden')
# else:
#     print ('Boek NIET gevonden')
    
    
# EASY
for i in range(1,11):
    print(i, end=' ')

som = 0
for i in range (1,11):
    if i % 2 == 1:
        som += i
print()
print(som)

invoer = int ( input('Geef een geheel getal in: ') )
priem = True

for i in range (2, invoer):
    #print('teller = ', i)
    if invoer % i == 0:
        priem = False 

if priem:
    print('{} is een priemgetal'.format(invoer))
else:    
    print('{} is NIET een priemgetal'.format(invoer))
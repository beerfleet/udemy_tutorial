nummer = int ( input('Geef een nummer in: ') )
compare_number = 51

if nummer < compare_number:
    print('{} is kleiner dan {}'.format(nummer, compare_number))
else:
    print('{} is groter dan {}'.format(nummer, compare_number))
    
if nummer % 2 == 0:
    print ('{} is even'.format(nummer))
else:
    print ('{} is oneven'.format(nummer))
    
if nummer % 10 == 0 and nummer % 50 == 0:
    if nummer % 30 == 0:
        print ('{} is deelbaar door 10, 30 en 50'.format(nummer))
    else:
        print ('{} is deelbaar door 10, 50 MAAR NIET door 30'.format(nummer))
elif nummer % 30 == 0:
    print ('{} is enkel deelbaar door 30'.format(nummer))
else:
    print ('{} is NIET deelbaar door 10, 30 of 50'.format(nummer))
